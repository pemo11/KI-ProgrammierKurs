#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filsoe: Unsplash_Download.py

import requests
import os
from pathlib import Path
import time
import json

class UnsplashDownloader:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.unsplash.com"
        self.headers = {
            "Authorization": f"Client-ID {api_key}"
        }
        
    def search_photos(self, query, per_page=10, page=1):
        """
        Sucht Fotos über die Unsplash API
        """
        url = f"{self.base_url}/search/photos"
        params = {
            "query": query,
            "per_page": per_page,
            "page": page,
            "orientation": "landscape"  # Querformat bevorzugen
        }
        
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def download_image(self, photo_data, category, index, download_folder):
        """
        Lädt ein einzelnes Bild herunter
        """
        try:
            # Bild-URL (regular = ~1080px breit)
            image_url = photo_data["urls"]["regular"]
            
            # Dateiname erstellen
            photo_id = photo_data["id"]
            filename = f"{category}_{index:02d}_{photo_id}.jpg"
            filepath = f"{download_folder}/{category}/{filename}"
            
            # Bild herunterladen
            response = requests.get(image_url, timeout=15)
            response.raise_for_status()
            
            # Bild speichern
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            # Metadaten speichern (optional)
            metadata = {
                "id": photo_data["id"],
                "description": photo_data.get("description", ""),
                "alt_description": photo_data.get("alt_description", ""),
                "photographer": photo_data["user"]["name"],
                "photographer_url": photo_data["user"]["links"]["html"],
                "photo_url": photo_data["links"]["html"],
                "download_url": image_url
            }
            
            metadata_file = filepath.replace(".jpg", "_metadata.json")
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            return filename, True
            
        except Exception as e:
            print(f"✗ Fehler beim Download: {e}")
            return None, False
    
    def download_category_images(self, category, images_per_category, download_folder):
        """
        Lädt Bilder einer Kategorie herunter
        """
        print(f"\nKategorie: {category}")
        
        # Ordner erstellen
        Path(f"{download_folder}/{category}").mkdir(exist_ok=True)
        
        downloaded_count = 0
        page = 1
        
        while downloaded_count < images_per_category:
            try:
                # Fotos suchen
                search_results = self.search_photos(
                    category, 
                    per_page=min(30, images_per_category - downloaded_count),
                    page=page
                )
                
                if not search_results["results"]:
                    print(f"Keine weiteren Bilder für '{category}' gefunden.")
                    break
                
                # Bilder herunterladen
                for i, photo in enumerate(search_results["results"]):
                    if downloaded_count >= images_per_category:
                        break
                    
                    filename, success = self.download_image(
                        photo, category, downloaded_count + 1, download_folder
                    )
                    
                    if success:
                        downloaded_count += 1
                        print(f"✓ {filename} ({downloaded_count}/{images_per_category})")
                    
                    # Kurze Pause
                    time.sleep(0.3)
                
                page += 1
                
            except Exception as e:
                print(f"✗ Fehler bei Kategorie {category}: {e}")
                break
        
        return downloaded_count
    
    def download_diverse_collection(self, total_images=100):
        """
        Lädt eine diverse Sammlung von Bildern herunter
        """
        categories = [
            "cats", "dogs", "cars", "flowers", "mountains", 
            "ocean", "food", "architecture", "people", "nature",
            "technology", "art", "travel", "city", "animals",
            "sunset", "forest", "beach", "coffee", "books"
        ]
        
        download_folder = "unsplash_images"
        Path(download_folder).mkdir(exist_ok=True)
        
        images_per_category = total_images // len(categories)
        total_downloaded = 0
        
        print(f"Lade {images_per_category} Bilder pro Kategorie herunter...")
        print(f"Gesamt: {total_images} Bilder aus {len(categories)} Kategorien")
        
        for category in categories:
            downloaded = self.download_category_images(
                category, images_per_category, download_folder
            )
            total_downloaded += downloaded
            
            # Kurze Pause zwischen Kategorien
            time.sleep(1)
        
        print(f"\n🎉 Fertig! {total_downloaded} Bilder heruntergeladen.")
        print(f"Gespeichert in: {os.path.abspath(download_folder)}")
        
        return total_downloaded
    
    def download_custom_categories(self, categories, images_per_category=10):
        """
        Lädt Bilder aus benutzerdefinierten Kategorien herunter
        """
        download_folder = os.path.join(os.path.dirname(__file__), "unsplash-images")
        print(f"Lade Bilder aus benutzerdefinierten Kategorien: {categories}")
        Path(download_folder).mkdir(exist_ok=True)
        
        total_downloaded = 0
        
        for category in categories:
            downloaded = self.download_category_images(
                category, images_per_category, download_folder
            )
            total_downloaded += downloaded
            time.sleep(1)
        
        print(f"\n✨ {total_downloaded} Bilder heruntergeladen!")
        return total_downloaded

def main():
    print("Unsplash API Downloader")
    print("=" * 30)
    
    # API-Key abfragen
    api_key = "FRnHR0xslriZ3F0qEtaUtNXmqAkMoQH8d6GeHOPPaM4"

    downloader = UnsplashDownloader(api_key)
    
    # Test der API-Verbindung
    try:
        test_result = downloader.search_photos("test", per_page=1)
        print("✅ API-Verbindung erfolgreich!")
    except Exception as e:
        print(f"❌ API-Fehler: {e}")
        return
    
    # Auswahlmenü
    print("\nOptionen:")
    print("1) 100 Bilder aus 20 verschiedenen Kategorien")
    print("2) Eigene Kategorien definieren")
    
    choice = input("\nWahl (1 oder 2): ").strip()
    
    if choice == "1":
        downloader.download_diverse_collection(100)
    elif choice == "2":
        categories_input = input("Kategorien (kommagetrennt): ").strip()
        categories = [cat.strip() for cat in categories_input.split(",")]
        count = int(input("Bilder pro Kategorie: ") or "10")
        downloader.download_custom_categories(categories, count)
    else:
        print("Ungültige Wahl. Führe Standard-Download aus...")
        downloader.download_diverse_collection(100)

if __name__ == "__main__":
    main()