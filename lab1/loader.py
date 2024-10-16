import time
import os
import sys
from tqdm import tqdm

for i in tqdm(range(10)):
    time.sleep(0.1)

print(f"Katalog roboczy: {os.getcwd()}")
print(f"Lokalizacja interpretera: {sys.executable}")
print(f"Wersja interpretera: {sys.version}")
print(f"Ścieżki wyszukiwania bibliotek: {sys.path}")
