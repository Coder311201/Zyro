# Zyro
![Logo](../icon.png)

Zyro ist eine kleine eigene Programmiersprache mit einem interaktiven Modus
und der Moeglichkeit, `.zr`-Dateien auszufuehren.

## Starten

### Linux

Interaktiven Modus starten:

```bash
python3 Zyro/main.py
```

Eine `.zr`-Datei ausfuehren:

```bash
python3 Zyro/main.py Skript.zr
```

### Windows

Interaktiven Modus starten:

```bat
python3 Zyro/main.py
```

Eine `.zr`-Datei ausfuehren:

```bat
python3 Zyro/main.py Skript.zr
```

## Abhaengigkeiten

In `functions.py` wird das externe Modul `colorama` benutzt. Es gehoert nicht zur Python-Standardbibliothek und muss installiert sein:

```bash
pip install colorama
```

## Befehle

Hilfe anzeigen:

```text
?hilfe
?
```

Text ausgeben:

```text
sage Hallo Welt
```

Farbig ausgeben:

```text
sage -f r Roter Text
sage -f g Gruener Text
sage -f b Blauer Text
```

Leerzeile ausgeben:

```text
sage -n
```

Eine Zyro-Datei aus dem Live-Modus ausfuehren:

```text
run -p Skript.zr
```

Warten:

```text
warte
warte -t 2
warte -t -ms_mode 500
```

Kommentar schreiben:

```text
> Das ist ein Kommentar
```

Programm beenden:

```text
exit
```

## Beispiel fuer eine `.zr`-Datei

```text
> Kleines Beispielprogramm
sage Hallo aus Zyro!
sage -n
sage -f g Das ist gruen.
warte -t 1
sage Fertig.
```
