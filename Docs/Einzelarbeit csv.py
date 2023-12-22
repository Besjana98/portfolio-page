import sys

# Öffnen der Datei
try:
    d = open("Telefonliste.csv","r+")
except:
    print("Datei konnte nicht geöffnet werden. Erneut versuchen")
    sys.exit(0)

# Hauptprogramm
print("Telefonliste:\n")
while True:
    # Hauptmenü, Auswahl
    try:
        menu = int(input("Was möchten Sie machen? Bitte Nummer eingeben "
            "(0: vorhandene Telefonliste anzeigen, 1: Kontakt suchen, 2: neuen Eintrag erstellen, "
                         "3: vorhandenen Eintrag ändern, 4: vorhandenen Eintrag löschen): "))
    except:
        print("Falsche Eingabe")

        continue

    #Menü 0 Telefonliste anzeigen
    if menu == 0:
        #Datei öffnen
        try:
            d = open("Telefonliste.csv", "r")
        except:
            print("Datei konnte nicht geöffnet werden.")
            sys.exit(0)
        for Liste in d.readlines():
            print(Liste)
    d.close()

    #Menü 1 Kontakt suchen:
    if menu == 1:
        # Datei öffnen
        while True:
            try:
                d = open("Telefonliste.csv", "r")
            except:
                print("Datei konnte nicht geöffnet werden.")
                sys.exit(0)

            suche = input("Bitte geben Sie den Vornamen, Nachnamen oder die Telefonnummer (+41...) ein:")
            if suche in d:
                    print("Kontakt:\n", d.read[suche].splitlines())
            else:
                print("Der Kontakt konnte mir Ihrer eingabe:", suche, "konnte nicht gefunden werden. "
                                                                  "Bitte versuchen Sie es erneut.")
            d.close()

    # Menü 2 neuen Eintrag erstellen:
    if menu == 2:
        #Datei öffnen
        try:
            d = open("Telefonliste.csv", "r")
        except:
            print("Datei konnte nicht geöffnet werden")
            sys.exit(0)

        #Kontakt hinzufügen
        kontakt = input("Bitte Geben Sie die Kontaktdaten wie folgt ein: Vorname, Nachname, Telefonnummer (+41...).")
        d.appende("\n",kontakt)
        d.close()
        #Kontak konnte erfolgreich eingefügt werden.

    # Menü 3 vorhandenen Eintrag ändern
    if menu == 3:
        while True:
            try:
                d = open("Telefonliste.csv", "r")
            except:
                print("Datei konnte nicht geöffnet werden")
                sys.exit(0)
            text = d.read()
            alt = str(input("Geben Sie den Kontakt (Vornamen, Nachnamen oder Telefonnumer) ein, "
                            "den Sie ändern möchten."))
            if alt in d:
                print(d.read())    
                neu = str(input("Bitte geben Sie den neuen Nachnamen, Vornamen und oder die Telefonnummer an."))
                d.write(text.replace(alt, neu))
            else:
                print("Der Kontakt konnte nicht gefunden werden. Bitte versuche es erneut.")

            print("Der Kontakt wurde abgeändert.")
            d.close()

    # Menü 4 vorhandenen Eintrag löschen
    if menu == 4:
        while True:
            # Datei öffnen
            try:
                d = open("Telefonliste.csv", "r+")
            except:
                print("Datei konnte nicht geöffnet werden")
                sys.exit(0)

            # Eingabe
            loeschen = {input("Bitte geben Sie den Kontakt (Vornamen, Nachnamen und die Telefonnummer) an, den Sie löschen möchten:")}
            if loeschen in d:
                del loeschen
            else:
                print("Der Kontakt konnte nicht gefunden werden. Bitte versuche es erneut.")
            #Datei schliessen
            d.close()

# Schliessen und beenden der Datei
d.close()