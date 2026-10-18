import json
import urllib3
import requests

# Wyłączamy ostrzeżenia o braku weryfikacji SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://www.spaceappschallenge.org/api/v2/awards/2025/global-nominees/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}

print("Pobieram projekty z NASA Space Apps...")
try:
  # Dodano parametr verify=False, który omija błąd certyfikatu SSL
  response = requests.get(url, headers=headers, verify=False)
  print(f"Kod statusu odpowiedzi: {response.status_code}")

  if response.status_code == 200:
    data = response.json()
    with open("nasa_projects.json", "w", encoding="utf-8") as f:
      json.dump(data, f, ensure_ascii=False, indent=4)
    print("Sukces! Zapisano plik nasa_projects.json")
  else:
    print(f"Błąd serwera. Treść odpowiedzi: {response.text[:300]}")
except Exception as e:
  print(f"Wystąpił wyjątek: {e}")
