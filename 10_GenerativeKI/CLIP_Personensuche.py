#! usr/bin/python3
# -*- coding: utf-8 -*-
# file: CLIP_Personensuche_Verbessert.py
# Verbesserte CLIP-Personensuche mit korrekten Wahrscheinlichkeiten

from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import os
from os import path
import numpy as np

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

print("Modell geladen")

# Alle Bilder in einem Ordner laden
images = []
image_names = []

image_folder = path.join(path.dirname(__file__), "images")
for filename in os.listdir(image_folder):
    if filename.endswith(('.jpg', '.png')):
        img = Image.open(os.path.join(image_folder, filename))
        images.append(img)
        image_names.append(filename)

print("=" * 60)
print("VERBESSERTE PERSONENSUCHE")
print("=" * 60)

# Verschiedene Personen-Suchbegriffe
person_queries = [
    "children playing",
    "adult people", 
    "elderly people",
    "group of people",
    "person portrait"
]

# Basis-Kategorien für Kontext
base_categories = ["people", "animals", "vehicles", "buildings", "nature", "objects"]

all_person_results = {}

for query in person_queries:
    print(f"\nSuche: '{query}'")
    print("-" * 30)
    
    results = []
    
    for image, image_name in zip(images, image_names):
        # Query mit Basis-Kategorien vergleichen
        all_queries = [query] + base_categories
        
        inputs = processor(text=all_queries, images=[image], return_tensors="pt", padding=True)
        outputs = model(**inputs)
        probs = outputs.logits_per_image[0].softmax(dim=0).detach().numpy()

        # Score für den spezifischen Personen-Query
        person_score = probs[0]
        results.append((image_name, person_score))
        
    # Sortieren und anzeigen
    results.sort(key=lambda x: x[1], reverse=True)
    all_person_results[query] = results
    
    # Top 5 für diese Kategorie
    for i, (name, score) in enumerate(results[:5], 1):
        print(f"{i}. {name}: {score:.1%}")

# Gesamtauswertung: Bestes Personen-Bild über alle Queries
print("\n" + "=" * 40)
print("GESAMTAUSWERTUNG PERSONEN")
print("=" * 40)

# Höchster Personen-Score pro Bild
best_person_scores = {}
for query, results in all_person_results.items():
    for image_name, score in results:
        if image_name not in best_person_scores or score > best_person_scores[image_name][0]:
            best_person_scores[image_name] = (score, query)

# Nach bestem Score sortieren
sorted_person_results = sorted(best_person_scores.items(), key=lambda x: x[1][0], reverse=True)

print("Top 5 Personenbilder (Gesamtauswertung):")
for i, (image_name, (score, best_query)) in enumerate(sorted_person_results[:5], 1):
    print(f"{i}. {image_name}: {score:.1%} ('{best_query}')")

# Nur Bilder mit hoher Personen-Wahrscheinlichkeit
high_confidence = [(name, score, query) for name, (score, query) in sorted_person_results if score > 0.3]

print(f"\nBilder mit hoher Personen-Wahrscheinlichkeit (>30%): {len(high_confidence)}")
for name, score, query in high_confidence[:5]:
    print(f"  {name}: {score:.1%} ('{query}')")