import json
import requests

url = "https://www.spaceappschallenge.org/api/v2/awards/2025/global-nominees/"

print("Pobieram projekty z NASA Space Apps...")
response = requests.get(url)

if response.status_code == 200:
  data = response.json()
  with open("nasa_projects.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
  print("Sukces! Zapisano plik nasa_projects.json")
else:
  print(
      "Błąd podczas pobierania danych. Kod statusu:",
      response.status_code,
  )
