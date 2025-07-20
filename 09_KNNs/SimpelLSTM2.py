#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# file: SimpelLSTM2.py

import numpy as np
import yaml
import re
from collections import Counter
from os import path
import warnings
import json
# Ignore deprecation warning for `input_length` argument in Embedding
warnings.filterwarnings("ignore", message="Argument `input_length` is deprecated.*")

from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Embedding
from keras.optimizers import Adam
from keras.utils import to_categorical

class SimpleLSTM:

    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        self.word_to_idx = {}
        self.idx_to_word = {}
        self.vocab_size = 0
        self.model = None
        # Epochenzahl aus Config sicher als Integer parsen
        self.epochs = int(self.config.get('epochs', 1))
        # Vokabular-Datei aus Config
        self.vocab_file = self.config.get('vocab_file')
        
        # Versuche, ein vorhandenes Modell zu laden
        model_file = self.config.get('model_file')
        if model_file:
            model_path = path.join(path.dirname(__file__), model_file)
            if path.exists(model_path):
                self.load_model(model_path)
                # Lade Vokabular, wenn definiert
                if self.vocab_file:
                    vocab_path = path.join(path.dirname(__file__), self.vocab_file)
                    if path.exists(vocab_path):
                        self.load_vocab(vocab_path)

    def save_model(self, model_path):
        """Speichert das trainierte Keras-Modell"""
        self.model.save(model_path)
        print(f"Modell gespeichert: {model_path}")
        # Speichere Vokabular
        if self.vocab_file:
            vocab_path = path.join(path.dirname(__file__), self.vocab_file)
            with open(vocab_path, 'w', encoding='utf-8') as f:
                json.dump(self.word_to_idx, f, ensure_ascii=False)
            print(f"Vokabular gespeichert: {vocab_path}")

    def load_model(self, model_path):
        """Lädt ein gespeichertes Keras-Modell"""
        self.model = load_model(model_path)
        print(f"Modell geladen: {model_path}")
    
    def load_vocab(self, vocab_path):
        """Lädt das gespeicherte Vokabular"""
        with open(vocab_path, 'r', encoding='utf-8') as f:
            word_to_idx = json.load(f)
        self.word_to_idx = word_to_idx
        self.idx_to_word = {idx: word for word, idx in word_to_idx.items()}
        self.vocab_size = len(self.word_to_idx)
        print(f"Vokabular geladen: {vocab_path}")

    def preprocess_text(self, text):
        """Einfache Textbereinigung"""
        text = text.lower()
        # Erlaube auch deutsche Umlaute und ß
        text = re.sub(r'[^a-zA-ZäöüÄÖÜß\s]', '', text)
        return text.split()

    def create_vocabulary(self, words):
        """Erstellt Vokabular aus Wörtern"""
        word_counts = Counter(words)
        min_count = self.config.get('min_count', 1)
        vocab_words = [w for w, c in word_counts.items() if c >= min_count]
        vocab_words = ['<UNK>'] + vocab_words
        
        self.word_to_idx = {word: idx for idx, word in enumerate(vocab_words)}
        self.idx_to_word = {idx: word for idx, word in enumerate(vocab_words)}
        self.vocab_size = len(vocab_words)
        print(f"Vokabulargröße: {self.vocab_size}")

    def prepare_sequences(self, words):
        """Erstellt Trainingssequenzen"""
        sequences = []
        seq_len = self.config['sequence_length']
        for i in range(len(words) - seq_len):
            seq = [ self.word_to_idx.get(words[i+j], self.word_to_idx['<UNK>'])
                    for j in range(seq_len+1) ]
            sequences.append(seq)
        X = np.array([s[:-1] for s in sequences])
        y = np.array([s[-1] for s in sequences])
        y = to_categorical(y, num_classes=self.vocab_size)
        return X, y

    def build_model(self):
        """Erstellt das LSTM-Modell"""
        model = Sequential([
            Embedding(self.vocab_size, self.config['embedding_dim'], 
                      input_length=self.config['sequence_length']),
            LSTM(self.config['lstm_units']),
            Dense(self.vocab_size, activation='softmax')
        ])
        optimizer = Adam(learning_rate=self.config['learning_rate'])
        model.compile(optimizer=optimizer, loss='categorical_crossentropy')
        self.model = model

    def train(self, text_file):
        """Trainiert das Modell"""
        print(f"Verwende Epochenzahl: {self.epochs}")
        with open(text_file, 'r', encoding='utf-8') as f:
            text = f.read()
        words = self.preprocess_text(text)
        self.create_vocabulary(words)
        X, y = self.prepare_sequences(words)
        self.build_model()
        print("Starte Training...")
        history = self.model.fit(
            X, y,
            epochs=self.epochs,
            batch_size=self.config['batch_size'],
            validation_split=self.config.get('validation_split', 0.1),
            verbose=1
        )
        print("Training abgeschlossen!")
        if 'val_loss' in history.history:
            final_val = history.history['val_loss'][-1]
            print(f"Finaler Validierungs-Loss: {final_val:.4f}")

    def predict_text(self, input_text, num_words=1):
        """Vorhersage der nächsten Wörter"""
        words = self.preprocess_text(input_text)
        seq_len = self.config['sequence_length']
        seed = words[-seq_len:] if len(words)>=seq_len else \
               words + ['<UNK>']*(seq_len-len(words))
        current = [ self.word_to_idx.get(w, self.word_to_idx['<UNK>']) for w in seed ]
        predictions = []
        for _ in range(num_words):
            probs = self.model.predict(np.array([current]), verbose=0)[0]
            probs[self.word_to_idx['<UNK>']] = 0
            probs = probs / probs.sum()
            top = np.argsort(probs)[-20:][::-1]
            print("Top 20 Vorhersagen und Wahrscheinlichkeiten:")
            for idx in top:
                print(f"{self.idx_to_word[idx]:<15} {probs[idx]:.4f}")
            pred_idx = int(np.argmax(probs))
            predictions.append({'word': self.idx_to_word[pred_idx], 'probability': float(probs[pred_idx])})
            current = current[1:]+[pred_idx]
        return predictions


def main():
    print("=== Einfaches LSTM Language Model (SimpelLSTM2) ===")
    yamlPath = path.join(path.dirname(__file__), "SimpelLSTM.yaml")
    lstm = SimpleLSTM(yamlPath)
    # Modell vorhanden? Wenn nicht, trainieren, sonst nur Vokabular erstellen
    text_file = lstm.config.get('text_file', 'TrainingText.txt')
    txtPath = path.join(path.dirname(__file__), text_file)
    if lstm.model is None:
        lstm.train(txtPath)
        model_file = lstm.config.get('model_file', 'SimpelLSTM.h5')
        save_path = path.join(path.dirname(__file__), model_file)
        lstm.save_model(save_path)
    else:
        print("Modell vorhanden, erstelle Vokabular...")
        with open(txtPath, 'r', encoding='utf-8') as f:
            text = f.read()
        words = lstm.preprocess_text(text)
        lstm.create_vocabulary(words)
        # Speichere Vokabular
        if lstm.vocab_file:
            vocab_path = path.join(path.dirname(__file__), lstm.vocab_file)
            with open(vocab_path, 'w', encoding='utf-8') as f:
                json.dump(lstm.word_to_idx, f, ensure_ascii=False)
            print(f"Vokabular gespeichert: {vocab_path}")
    # Vorhersage testen
    test_text = "Die Kinder spielten"
    print(f"\nEingabe: '{test_text}'")
    preds = lstm.predict_text(test_text, num_words=1)
    print("\nVorhersage:")
    for i,p in enumerate(preds,1): print(f"{i:2d}. {p['word']:<15} (Wahrscheinlichkeit: {p['probability']:.4f})")
    if preds:
        print(f"\nVollständiger Text: {test_text} {preds[0]['word']}")

if __name__ == "__main__":
    main()