import requests
import os
import time
from urllib.parse import urlparse
import json

class DogImageDownloader:
    def __init__(self, download_folder="hundebilder"):
        self.download_folder = download_folder
        self.pixabay_api_key = "YOUR_PIXABAY_API_KEY"  # Kostenlos auf pixabay.com registrieren
        
        # Ordner erstellen falls nicht vorhanden
        os.makedirs(self.download_folder, exist_ok=True)
    
    def download_from_pixabay(self, query="dog", count=50):
        """
        Lädt Bilder von Pixabay herunter
        """
        print(f"📥 Lade {count} Bilder von Pixabay herunter...")
        
        url = "https://pixabay.com/api/"
        params = {
            'key': self.pixabay_api_key,
            'q': query,
            'image_type': 'photo',
            'per_page': min(count, 200),  # Max 200 per request
            'category': 'animals',
            'min_width': 640,
            'min_height': 480,
            'safesearch': 'true'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            images = data.get('hits', [])
            print(f"✅ {len(images)} Bilder gefunden")
            
            for i, image in enumerate(images[:count]):
                self._download_image(
                    image['webformatURL'], 
                    f"pixabay_dog_{i+1}.jpg"
                )
                time.sleep(0.5)  # Rate limiting
                
        except requests.RequestException as e:
            print(f"❌ Fehler bei Pixabay: {e}")
    
    def download_from_dog_ceo(self, count=30):
        """
        Lädt Bilder von der kostenlosen Dog CEO API herunter
        (Keine API-Keys erforderlich, aber begrenzte Auswahl)
        """
        print(f"📥 Lade {count} Bilder von Dog CEO API herunter...")
        
        # Alle verfügbaren Rassen abrufen
        breeds_url = "https://dog.ceo/api/breeds/list/all"
        try:
            response = requests.get(breeds_url)
            response.raise_for_status()
            breeds_data = response.json()
            breeds = list(breeds_data['message'].keys())
            
            downloaded = 0
            
            for breed in breeds:
                if downloaded >= count:
                    break
                    
                # Bilder für diese Rasse abrufen
                images_url = f"https://dog.ceo/api/breed/{breed}/images"
                response = requests.get(images_url)
                
                if response.status_code == 200:
                    images_data = response.json()
                    images = images_data.get('message', [])
                    
                    # Maximal 3 Bilder pro Rasse
                    for img_url in images[:3]:
                        if downloaded >= count:
                            break
                            
                        filename = f"dogceo_{breed}_{downloaded + 1}.jpg"
                        self._download_image(img_url, filename)
                        downloaded += 1
                        time.sleep(0.3)
                        
        except requests.RequestException as e:
            print(f"❌ Fehler bei Dog CEO API: {e}")
    
    def _download_image(self, url, filename):
        """
        Hilfsfunktion zum Herunterladen eines einzelnen Bildes
        """
        try:
            response = requests.get(url, stream=True, timeout=10)
            response.raise_for_status()
            
            filepath = os.path.join(self.download_folder, filename)
            
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"✅ {filename} heruntergeladen")
            
        except requests.RequestException as e:
            print(f"❌ Fehler beim Download von {filename}: {e}")
    
    def create_zip(self, zip_filename="hundebilder.zip"):
        """
        Erstellt eine Zip-Datei aus allen heruntergeladenen Bildern
        """
        import zipfile
        
        print(f"📦 Erstelle Zip-Datei: {zip_filename}")
        
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for filename in os.listdir(self.download_folder):
                if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                    filepath = os.path.join(self.download_folder, filename)
                    zipf.write(filepath, filename)
        
        print(f"✅ Zip-Datei erstellt: {zip_filename}")

def main():
    """
    Hauptfunktion - Beispiel für die Verwendung
    """
    downloader = DogImageDownloader()
    
    print("🐕 Hundebilder Download Skript")
    print("=" * 40)
    
    # Option 1: Dog CEO API (kostenlos, keine Keys nötig)
    print("\n1️⃣ Verwende Dog CEO API (kostenlos, keine Registration):")
    downloader.download_from_dog_ceo(count=30)
    
    # Option 2: Pixabay (benötigt kostenlosen API Key)
    print("\n2️⃣ Verwende Pixabay (benötigt API Key):")
    if downloader.pixabay_api_key != "YOUR_PIXABAY_API_KEY":
        downloader.download_from_pixabay(count=35)
    else:
        print("⚠️ Pixabay API Key nicht gesetzt")
    
    # Option 3: Unsplash (benötigt kostenlosen API Key)
    print("\n3️⃣ Verwende Unsplash (benötigt API Key):")
    if downloader.unsplash_access_key != "YOUR_UNSPLASH_ACCESS_KEY":
        downloader.download_from_unsplash(count=35)
    else:
        print("⚠️ Unsplash API Key nicht gesetzt")
    
    # Zip-Datei erstellen
    print("\n📦 Erstelle Zip-Datei...")
    downloader.create_zip()
    
    print("\n🎉 Fertig! Alle Bilder wurden heruntergeladen.")

if __name__ == "__main__":
    # Benötigte Pakete installieren:
    # pip install requests
    
    main()

# ANLEITUNG ZUR VERWENDUNG:
# 
# 1. Installiere requests: pip install requests
# 
# 2. API Keys besorgen (kostenlos):
#    - Pixabay: Registriere dich auf pixabay.com und hole dir einen API Key
#    - Unsplash: Gehe zu unsplash.com/developers und erstelle eine App
# 
# 3. Setze die API Keys in den Variablen ein
# 
# 4. Führe das Skript aus: python hundebilder_downloader.py
#
# 5. Das Skript lädt Bilder in den Ordner "hundebilder" herunter
#    und erstellt automatisch eine Zip-Datei
#
# OHNE API Keys funktioniert die Dog CEO API (bis zu ~100 Bilder verfügbar)