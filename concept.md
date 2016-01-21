# Eine Analyse meines (bisherigen) Bewerbungsprozesses

#### Bisher besteht mein Bewerbungsprozeß aus folgenden Schritten:
1. Stellenanzeigen sichten und eine Auswahl treffen.
2. git branch und entsprechende Ordner anlegen
3. Daten in den Ordner kopieren: mindestens Anschreiben-Template und Ausschreibungs-Template, ggf. Lebenslauf, ggf. Arbeitsprobe(n)
4. Die Stelle mit den notwendigen Daten erfassen (Adressdaten, Ansprechperson, job title, Referenznummer etc.)
5. ggf. Lebenslauf ergänzen (und, falls noch nicht geschehen, in den Ordner kopieren, wenn er auf die Stelle angepaßt wird)
6. Anschreiben mit den notwendigen Daten aus Punkt 4 versehen
7. Anschreiben-Text modifizieren
8. Rechtschreibprüfung mit aspell
9. pdf generieren, Korrekturlauf
10. Dokumente zu einem pdf zusammenfassen
11. Quelltext des Anschreibens mittels detex zu Reintextdatei verwandeln, Informationen "strippen" (unnötige Zeilen entfernen, nur Anrede und Body Text des Schreibens sollen erhalten bleiben)
12. E-Mail schreiben oder 12a: Drucken (+versandfertig machen)
13. Nachverfolgung

#### Daraus resultiert folgendes Vorgehen:
* Schritte 7 bis 9 sind iterativ.
* Für Schritt 2 und 3: bash-script
* Schritt 6: Da ich LaTeX verwende, bietet es sich an, die LaTex-Datei mit string formatters zu versehen und diese mittels eines Python-Skripts, das aus einer weiteren Datei (csv?) liest, anzusprechen sowie das Resultat in eine weitere LaTeX-Datei zu exportieren. Sobald dieser Teil umgesetzt ist, kann ggf. das Skript für 2/3 entfallen.
* Schritt 9: Lediglich ein pdflatex-Befehl, ergänzt um "Aufräumen" (Löschen von unnötigen Dateien).
* Schritt 10: bash-script, das pdfjam und mv aufruft (für die ansprechende, "arbeitgebertaugliche" Benennung)
* Schritt 11: detex und Kürzen der Datei mittels regex oder shell-Operation
* Schritt 12: Aufruf von Thunderbird mit Optionen (E-Mail-Adresse, Subject, body, attachment) per Shell
* noch zu überlegen: An welchen Stellen sind automatische git-Operationen sinnvoll?


