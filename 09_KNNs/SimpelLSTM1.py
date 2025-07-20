#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# file: SimpelLSTM1.py

import numpy as np
import yaml
import re
from collections import Counter
from os import path
import warnings
# Ignore deprecation warning for `input_length` argument in Embedding
warnings.filterwarnings("ignore", message="Argument `input_length` is deprecated.*")

from keras.models import Sequential
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
    
    def preprocess_text(self, text):
        """Einfache Textbereinigung"""
        text = text.lower()
        # Erlaube auch deutsche Umlaute und ß
        text = re.sub(r'[^a-zA-ZäöüÄÖÜß\s]', '', text)
        return text.split()
    
    def create_vocabulary(self, words):
        """Erstellt Vokabular aus Wörtern"""
        word_counts = Counter(words)
        vocab_words = [word for word, count in word_counts.items() if count >= 2]
        min_count = self.config.get('min_count', 1)
        vocab_words = [w for w, c in word_counts.items() if c >= min_count]
        vocab_words = ['<UNK>'] + vocab_words
        
        self.word_to_idx = {word: idx for idx, word in enumerate(vocab_words)}
        self.idx_to_word = {idx: word for idx, word in enumerate(vocab_words)}
        self.vocab_size = len(vocab_words)
        
        print(f"Vokabulargröße: {self.vocab_size}")
        # POS-Filter entfernt; alle Wörter außer <UNK> werden erlaubt

    def prepare_sequences(self, words):
        """Erstellt Trainingssequenzen"""
        sequences = []
        seq_len = self.config['sequence_length']
        
        for i in range(len(words) - seq_len):
            seq = []
            for j in range(seq_len + 1):
                word = words[i + j]
                if word in self.word_to_idx:
                    seq.append(self.word_to_idx[word])
                else:
                    seq.append(self.word_to_idx['<UNK>'])
            sequences.append(seq)
        
        X = np.array([seq[:-1] for seq in sequences])
        y = np.array([seq[-1] for seq in sequences])
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
        # Text laden
        with open(text_file, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Preprocessing
        words = self.preprocess_text(text)
        self.create_vocabulary(words)
        
        # Sequenzen erstellen
        X, y = self.prepare_sequences(words)
        
        # Modell erstellen
        self.build_model()
        
        # Training
        print("Starte Training...")
        history = self.model.fit(
            X, y,
            epochs=self.epochs,
            batch_size=self.config['batch_size'],
            validation_split=self.config.get('validation_split', 0.1),  # Standard Fit-Ausgabe zeigt loss und val_loss
            verbose=1
        )
        print("Training abgeschlossen!")
        # Finaler Validierungs-Loss
        if 'val_loss' in history.history:
            final_val_loss = history.history['val_loss'][-1]
            print(f"Finaler Validierungs-Loss: {final_val_loss:.4f}")
    
    def predict_text(self, input_text, num_words=1):
        """Vorhersage der nächsten Wörter"""
        words = self.preprocess_text(input_text)
        
        # Letzten sequence_length Wörter nehmen
        if len(words) >= self.config['sequence_length']:
            seed_words = words[-self.config['sequence_length']:]
        else:
            seed_words = words + ['<UNK>'] * (self.config['sequence_length'] - len(words))
        
        # Zu Indizes konvertieren
        seed_sequence = []
        for word in seed_words:
            if word in self.word_to_idx:
                seed_sequence.append(self.word_to_idx[word])
            else:
                seed_sequence.append(self.word_to_idx['<UNK>'])
        
        predictions = []
        current_sequence = seed_sequence.copy()
        
        for _ in range(num_words):
            # Modellvorhersage
            X = np.array([current_sequence])
            probs = self.model.predict(X, verbose=0)[0]
            # <UNK> ausschließen und neu normieren
            unk_idx = self.word_to_idx['<UNK>']
            probs[unk_idx] = 0
            probs = probs / probs.sum()
            # Top-20 Wahrscheinlichkeiten ausgeben
            top_indices = np.argsort(probs)[-20:][::-1]
            print("Top 20 Vorhersagen und Wahrscheinlichkeiten:")
            for idx in top_indices:
                print(f"{self.idx_to_word[idx]:<15} {probs[idx]:.4f}")
            # Wort mit maximaler Wahrscheinlichkeit wählen
            predicted_idx = int(np.argmax(probs))
            predicted_word = self.idx_to_word[predicted_idx]
            probability = float(probs[predicted_idx])
         
            predictions.append({
                'word': predicted_word,
                'probability': probability
            })
            # Sequenz aktualisieren
            current_sequence = current_sequence[1:] + [predicted_idx]
        
        return predictions

# Hauptprogramm
def main():
    print("=== Einfaches LSTM Language Model ===")
    
    # Modell erstellen
    yamlPath = path.join(path.dirname(__file__), "SimpelLSTM.yaml")
    lstm = SimpleLSTM(yamlPath)
    
    # Training: Textdateipfad aus YAML einlesen
    text_file = lstm.config.get('text_file', 'AlicesImWunderland.txt')
    txtPath = path.join(path.dirname(__file__), text_file)
    lstm.train(txtPath)
    
    # Vorhersage testen
    test_text = "Alice fing an sich zu"
    print(f"\nEingabe: '{test_text}'")
    
    predictions = lstm.predict_text(test_text, num_words=1)
    
    print("\nVorhersage:")
    for i, pred in enumerate(predictions, 1):
        print(f"{i:2d}. {pred['word']:<15} (Wahrscheinlichkeit: {pred['probability']:.4f})")
    
    # Vollständiger Text
    predicted_word = predictions[0]['word'] if predictions else ''
    full_text = test_text + " " + predicted_word
    print(f"\nVollständiger Text: {full_text}")

if __name__ == "__main__":
    main()