#! usr/bin/python3
# -*- coding: utf-8 -*-
# filsoe: CLIP_Beispiel1.py
# Eine einfache CLIP-Kategorisierung von Bildern

#! usr/bin/python3
# -*- coding: utf-8 -*-
# file: CLIP_Kategorisierung1.py
# Eine einfache CLIP-Kategorisierung

from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import os
from os import path

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Alle Bilder in einem Ordner laden
images = []
image_names = []

image_folder = path.join(path.dirname(__file__), "images")
for filename in os.listdir(image_folder):
    if filename.endswith(('.jpg', '.png')):
        img = Image.open(os.path.join(image_folder, filename))
        images.append(img)
        image_names.append(filename)

# Kategorien definieren (statt einem Suchbegriff)
categories = ["a cat", "a dog", "a car", "a flower", "a person", "nature", "food"]

print(f"Kategorisiere {len(images)} Bilder in {len(categories)} Kategorien...")
print("-" * 50)

# Jedes Bild einzeln kategorisieren
for i, image_name in enumerate(image_names):
    # Einzelnes Bild mit allen Kategorien vergleichen
    single_image = [images[i]]
    inputs = processor(text=categories, images=single_image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    
    # Wahrscheinlichkeiten berechnen
    probs = outputs.logits_per_image[0].softmax(dim=0)
    best_category_idx = probs.argmax()
    best_category = categories[best_category_idx]
    confidence = probs[best_category_idx]
    
    print(f"{image_name} -> {best_category} ({confidence:.1%})")

print("-" * 50)

# Zusammenfassung: Anzahl pro Kategorie
category_counts = {}
for i, image_name in enumerate(image_names):
    single_image = [images[i]]
    inputs = processor(text=categories, images=single_image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    
    probs = outputs.logits_per_image[0].softmax(dim=0)
    best_category = categories[probs.argmax()]
    
    if best_category in category_counts:
        category_counts[best_category] += 1
    else:
        category_counts[best_category] = 1

print("Zusammenfassung:")
for category, count in category_counts.items():
    print(f"{category}: {count} Bilder")

