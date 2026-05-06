<div align="center">
  <img src="assets/icon.png" width="300">
</div>

Z ist eine kleine eigene Programmiersprache mit einem interaktiven Modus
und der Möglichkeit, `.zr`-Dateien auszuführen.

## Starten

### Linux

Interaktiven Modus starten:

```bash
python3 Z/main.py
```

Eine `.zr`-Datei auszuführen:

```bash
python3 Z/main.py Skript.zr
```

### Windows

Interaktiven Modus starten:

```bat
python3 Z/main.py
```

Eine `.zr`-Datei auszuführen:

```bat
python3 Z/main.py Skript.zr
```

## Abhängigkeiten

In `functions.py` wird das externe Modul `colorama` benutzt. Es gehört nicht zur Python-Standardbibliothek und muss installiert sein:

```bash
pip install colorama
```

## Befehle

Hilfe anzeigen:

```text
?hilfe
?
```

### Text ausgeben:

```text
sage Hallo Welt
```

Farbig ausgeben:

```text
sage -f r Roter Text
sage -f g Grüner Text
sage -f b Blauer Text
```

Leerzeile ausgeben:

```text
sage -n
```

### Eine Z-Datei aus dem Live-Modus ausfuehren:

```text
run -p Skript.zr
```

### Warten:

```text
warte
warte -t 2
warte -t -ms_mode 500
```

### Variablen:

```
<var_name> => <var_value>
```
Beispiel:
```
begruesung => Hallo, und willkommen in Zyro
sage begruesung 
```
Ausgabe: Hallo, und willkommen in Zyro

### Kommentar schreiben:

```text
> Das ist ein Kommentar
```

### Programm beenden:

```text
exit
```

## Beispiel für eine `.zr`-Datei

```text
> Kleines Beispielprogramm
sage Hallo aus Z!
sage -n
sage -f g Das ist grün.
warte -t 1
sage Fertig.
```
