# Coffee Machine — `test.py`

Kurzbeschreibung

Ein kleines interaktives Python-Skript, das eine einfache Kaffeemaschinen-Simulation zeigt. Das Programm fragt den Operator nach einem kurzen Report, erlaubt das Ausschalten der Maschine, nimmt Bestellungen (espresso/latte/cappuccino), prüft Ressourcen, akzeptiert Münzen und gibt Wechselgeld zurück.

Datei

- `test.py` — Enthält alle Funktionen und eine `main()`-Schleife. Die wichtigsten Funktionen sind:
  - `ressoure_report()` — initialisiert Ressourcen (Wasser, Milch, Kaffee, Geld) und kann einen Report ausgeben
  - `turn_coffemachine_off()` — fragt den Operator, ob die Maschine ausgeschaltet werden soll
  - `user_input()` — fragt den Kunden nach dem gewünschten Getränk (validiert Eingabe)
  - `ressource_check(choice, all_ressources)` — prüft, ob genügend Zutaten vorhanden sind
  - `coin_machine()` — nimmt Münzeingaben (Quart., Dimes, Nickles, Pennies) und berechnet die Summe
  - `check_transaction(total, choice)` — vergleicht gezahlten Betrag mit Preis, gibt Wechselgeld oder storniert

Voraussetzungen

- Python 3.x (ausführbar mit `python3`)
- Keine externen Bibliotheken erforderlich

Ausführen

Wechsle in das Verzeichnis, das `test.py` enthält, und starte das Skript:

```bash
python3 /Users/theodorlaukart/Documents/GitHub/UdemyCourses/Python_100_days/day_15/test.py
```

Ablauf beim Start

1. `ressoure_report()` wird aufgerufen. Wenn du `report` eintippst, zeigt es die Startwerte für Wasser, Milch, Kaffee und Geld.
2. Das Programm fragt, ob der Operator die Maschine ausschalten möchte. Tippe `off`, um das Programm zu beenden.
3. Der Kunde wird nach seinem Getränk gefragt (`espresso`, `latte` oder `cappuccino`).
4. Das Programm prüft die Ressourcen und gibt eine Meldung, ob das Getränk zubereitet werden kann.
5. Es folgt die Abfrage der Münzen: Anzahl Quarters, Dimes, Nickles und Pennies.
6. Das Programm rechnet den Gesamtbetrag, prüft den Preis und gibt entsprechendes Wechselgeld oder eine Rückerstattungsmeldung aus.
7. Die Schleife wiederholt sich, bis `off` eingegeben wird.

Bekannte Einschränkungen / Vorschläge

- Ressourcen werden beim Kauf aktuell noch nicht abgezogen. Das Skript prüft nur, ob genug vorhanden ist.
- Der `money`-Wert wird beim Kauf nicht aktualisiert.
- Die Funktionen haben kleinere Tippfehler in den Namen (`ressoure_*`, `ressource_*`) — du kannst sie umbenennen, falls erwünscht.
- Verbesserungen, die leicht ergänzt werden können:
  - Zutaten beim erfolgreichen Kauf von `all_ressources` abziehen.
  - `money` in `all_ressources` erhöhen, wenn ein Kauf erfolgreich ist.
  - Bessere Fehlerbehandlung für nicht-numerische Münz-Eingaben.
  - Unit-Tests für Kernfunktionen.

Beispiel-Session (Kurz):

- Starte Skript → wenn nach Report gefragt, tippe `report` oder Enter.
- Operator: tippe Enter (nicht `off`).
- Kunde: `latte` → Programm prüft Ressourcen.
- Bei ausreichenden Ressourcen → gib Münzen ein (z. B. Quarters: 10, Dimes: 0, Nickles: 0, Pennies: 0).
- Programm zeigt Wechselgeld und Ausgabe-Meldung.

Nächste Schritte (optional)

Wenn du möchtest, implementiere ich:
- Ressourcen-Deduction und Geld-Update in `all_ressources`.
- Robustere Eingabeprüfung für Münzen.
- Umbenennung der Funktionen auf korrektes Englisch (`resource_report`, `resource_check`).

Lizenz

Frei zur Verwendung für Lernzwecke.

---

Erstellt für das Projekt in:
`/Users/theodorlaukart/Documents/GitHub/UdemyCourses/Python_100_days/day_15`
