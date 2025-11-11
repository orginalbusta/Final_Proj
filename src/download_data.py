"""
Download sample datasets from the World Bank Data by Indicators repository
"""
import urllib.request
import os

# Base URL for the GitHub repository
BASE_URL = "https://raw.githubusercontent.com/light-and-salt/World-Bank-Data-by-Indicators/master"

# Key indicators to download for our explorable explanation
INDICATORS = {
    'climate-change': 'climate-change.csv',
    'economy-and-growth': 'economy-and-growth.csv',
    'education': 'education.csv',
    'health': 'health.csv',
    'poverty': 'poverty.csv',
    'infrastructure': 'infrastructure.csv'
}

def download_data():
    """Download selected indicator datasets"""
    data_dir = '../data'
    os.makedirs(data_dir, exist_ok=True)
    
    for indicator, filename in INDICATORS.items():
        url = f"{BASE_URL}/{indicator}/{filename}"
        output_path = os.path.join(data_dir, filename)
        
        print(f"Downloading {indicator}...")
        try:
            urllib.request.urlretrieve(url, output_path)
            print(f"  [OK] Saved to {output_path}")
        except Exception as e:
            print(f"  [ERROR] Error: {e}")
    
    print("\nDownload complete!")

if __name__ == "__main__":
    download_data()

