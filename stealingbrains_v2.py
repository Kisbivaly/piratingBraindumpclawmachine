import requests

# Az URL alapformátuma
base_url = "https://aipwidgets.click/claw/Assets/Img/brain{}_v2.gif"

# Bejárás a számok között (0-tól 100-ig)
for i in range(9):
    url = base_url.format(i)
    try:
        response = requests.get(url, timeout=10)
        # Ellenőrzés: ha sikeres a kérés (200-as státusz)
        if response.status_code == 200:
            file_name = f"brain{i}_v2.gif"
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"Sikeresen letöltve: {file_name}")
        else:
            print(f"Nem található vagy átirányítva: {url}")
    except requests.RequestException as e:
        print(f"Hiba történt: {e} - {url}")
