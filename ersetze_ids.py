import os

def ersetze_id_in_json_dateien(basisverzeichnis, alt, neu):
    # Gehe rekursiv durch alle Dateien im Basisverzeichnis
    for root, _, files in os.walk(basisverzeichnis):
        for file in files:
            if file.endswith(".json"):
                dateipfad = os.path.join(root, file)
                try:
                    with open(dateipfad, "r", encoding="utf-8") as f:
                        inhalt = f.read()

                    if alt in inhalt:
                        inhalt_neu = inhalt.replace(alt, neu)
                        with open(dateipfad, "w", encoding="utf-8") as f:
                            f.write(inhalt_neu)
                        print(f"✔ Geändert: {dateipfad}")
                    else:
                        print(f"⏩ Keine Änderung: {dateipfad}")
                except Exception as e:
                    print(f"⚠ Fehler bei {dateipfad}: {e}")

# Anwendung
ersetze_id_in_json_dateien("schemas", "politpatrick", "patrickkunze")