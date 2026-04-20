# Pobieranie losowych artykułów z angielskiej Wikipedii do pliku JSON
import requests
import json

HEADERS = {"User-Agent": "MojaAplikacja/1.0 (kontakt@example.com)"}

def pobierz_losowe_tytuly(ile):
    params = {
        "action": "query",
        "list": "random",
        "rnnamespace": 0,
        "rnlimit": ile,
        "format": "json"
    }
    response = requests.get("https://en.wikipedia.org/w/api.php", params=params, headers=HEADERS)
    return [a["title"] for a in response.json()["query"]["random"]]

def czy_ujednoznaczniajaca(page):
    kategorie = [k["title"] for k in page.get("categories", [])]
    return any("disambiguation" in k.lower() for k in kategorie)

def pobierz_artykul(tytul, tylko_wstep=False):
    params = {
        "action": "query",
        "titles": tytul,
        "prop": "extracts|info|categories",
        "inprop": "url",
        "explaintext": True,
        "cllimit": 10,
        "format": "json"
    }
    if tylko_wstep:
        params["exintro"] = True

    response = requests.get("https://en.wikipedia.org/w/api.php", params=params, headers=HEADERS)
    pages = response.json()["query"]["pages"]
    page = next(iter(pages.values()))

    if czy_ujednoznaczniajaca(page):
        return None

    return {
        "tytul": page.get("title", ""),
        "tekst": page.get("extract", ""),
        "url": page.get("fullurl", "")
    }

# Użycie
wyniki = []
ile_chcemy = 500

while len(wyniki) < ile_chcemy:
    tytuly = pobierz_losowe_tytuly(ile_chcemy - len(wyniki))
    for tytul in tytuly:
        wstep = pobierz_artykul(tytul, tylko_wstep=True)
        if wstep is None:
            print(f"Pominięto (ujednoznaczniająca): {tytul}")
            continue
        pelny = pobierz_artykul(tytul, tylko_wstep=False)
        wyniki.append({
            "title": pelny["tytul"],
            "url": pelny["url"],
            "introduction": wstep["tekst"],
            "text": pelny["tekst"]
        })
        print(f"Pobrano: {pelny['tytul']}")

# Zapis do pliku JSON
with open("artykuly.json", "w", encoding="utf-8") as f:
    json.dump(wyniki, f, ensure_ascii=False, indent=2)

print(f"\nZapisano {len(wyniki)} artykułów do artykuly.json")