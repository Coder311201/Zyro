import functions
import importlib
import sys
from pathlib import Path


class Interpreter:
    def __init__(self, debug: bool = True):
        self._functions = functions.functions(debug)
        self._vars = {}
        self._libs = {}
        if debug:
            print("Interpreter is running")

    def execute(self, command: str):
        if not "=>" in command.split():
            for var in self._vars:
                var = str(var)
                if var in command:
                    command = command.replace(var, str(self._vars.get(var, None)))

        command_parts = self._functions.split_command(command)
        if not command_parts:
            return
        
        for i, part in enumerate(command_parts):
            if part in self._libs:
                if i + 1 >= len(command_parts):
                    self._functions.ausgabe("Fehler!", "r")
                    print(f"Keine Funktion fuer Bibleothek {part} genannt")
                    return
                if not hasattr(self._libs[part], command_parts[i + 1]):
                    self._functions.ausgabe("Fehler!", "r")
                    print(f"Die Funktion {command_parts[i + 1]} existiert in der Bibleothek {part} nicht")
                    return
                args = command_parts[i + 2:]
                methode = getattr(self._libs[part], command_parts[i + 1])
                try:
                    out = methode(*args)
                except TypeError:
                    self._functions.ausgabe("Fehler!", "r")
                    print("Zu wenig Argumente!")
                    return

                if out == None: return
                command_parts[i:] = [str(out)]
  
        if any(part in ["+", "-", "*", "/", "^", "(", ")"] for part in command_parts):
            command_parts = self._functions.calculate(command_parts)
            if command_parts is None:
                return
            

        cmd = command_parts[0]
        

        if cmd == "?hilfe" or cmd == "?":
            if len(command_parts) >= 2:
                if command_parts[1] == "-m":
                    print(
                    "+: Addieren\n" \
                    "-: Subtrahieren\n" \
                    "^: Potenzionieren\n" \
                    "*: Multiplikation\n" \
                    "/: Division")
                return
            print(
                "Willkommen im Z-Hilfsmenü\n"
                "Drücke ^C zum Beenden\n\n"
                "Befehle:\n"
                "  ?hilfe oder ?\n"
                "    Zeigt diese Hilfe an.\n" 
                "    -m: Zeigt Mathematikhilfe\n\n"
                "  sage <text>\n"
                "    Gibt den angegebenen Text aus.\n\n"
                "  sage -f <farbe> <text>\n"
                "    Gibt den Text farbig aus.\n"
                "    Farben: r = rot, g = gruen, b = blau\n\n"
                "  sage -n\n"
                "    Gibt eine Leerzeile aus.\n\n"
                "  run -p <datei.zr>\n"
                "    Fuehrt eine Z-Datei aus.\n\n"
                "  warte\n"
                "    Wartet 10 Sekunden.\n\n"
                "  warte -t <sekunden>\n"
                "    Wartet die angegebene Anzahl Sekunden.\n\n"
                "  warte -t -ms_mode <millisekunden>\n"
                "    Wartet die angegebene Anzahl Millisekunden.\n\n"
                "  > <kommentar>\n"
                "    Ignoriert die Zeile als Kommentar.\n" 
                "  <var_name> => <var_value>\n" 
                "  Definiert eine Variable mit dem angegebenen Namen und Wert.\n" 
                "  lade <Bileothek>\n" \
                "  Lädt eine Bibleothek"
            )

        elif cmd == "lade":
            if len(command_parts) == 1:
                self._functions.ausgabe("Fehler!", "r")
                print("Keine Bibleothek genannt")
                return
            elif len(command_parts) >= 3:
                self._functions.ausgabe("Fehler!", "r")
                print("Nur eine Bibleothek nennen")
                return
            
            bibo = str(command_parts[1])
            libs_ordner = Path(__file__).resolve().parent / "Z_libs"
            dateipfad = libs_ordner / f"{bibo}.py"
            if not dateipfad.exists():
                self._functions.ausgabe("Fehler!", "r")
                print(f"Die Bibleothek {bibo} existiert nicht!")
                return
            
            modul = importlib.import_module(f"Z_libs.{bibo}")                
            klasse = getattr(modul, bibo)
            self._libs[bibo] = klasse()

        elif "=>" in command_parts:
            if command_parts.index("=>") != 0:
                var_name = " ".join(command_parts[: command_parts.index("=>")])
                var_value = " ".join(command_parts[command_parts.index("=>") + 1:])
                var_value = str(var_value)
                self._vars[var_name] = var_value
            else:
                self._functions.ausgabe("Ungültiger Variablename!", "r")

        elif cmd == "sage":
            if len(command_parts) < 2:
                self._functions.ausgabe("Keine Argumente!", "r")
                print("Fuehre ?hilfe oder sage -h aus wenn du hilfe brauchst")
                return
            if command_parts[1] == "-f":
                if len(command_parts) < 4:
                    self._functions.ausgabe("Keine Farbe oder Text!", "r")
                    print("Fuehre ?hilfe oder sage -h aus wenn du hilfe brauchst")
                    return
                text = " ".join(command_parts[3:])
                self._functions.ausgabe(text, command_parts[2])
            elif command_parts[1] == "-h":
                print(
                    "Hilfe fuer sage\n"
                    "Verwendung:\n"
                    "  sage <text>\n"
                    "  sage -f <farbe> <text>\n"
                    "  sage -n\n\n"
                    "Farben:\n"
                    "  r = rot\n"
                    "  g = gruen\n"
                    "  b = blau"
                )

            elif command_parts[1] == "-n":
                print()

            else:
                text = " ".join(command_parts[1:])
                self._functions.ausgabe(text, "w")

        elif cmd == "run":
            if len(command_parts) < 2:
                self._functions.ausgabe("Keine Argumente!", "r")
                print("Fuehre ?hilfe oder run -h aus wenn du hilfe brauchst")
                return

            if command_parts[1] == "-p":
                if len(command_parts) < 3:
                    self._functions.ausgabe("Kein Pfad angegeben!", "r")
                    print("Fuehre ?hilfe oder run -h aus wenn du hilfe brauchst")
                    return
                self._functions.compile(command_parts[2])
            elif command_parts[1] == "-h":
                print(
                    "Hilfe fuer run\n"
                    "Verwendung:\n"
                    "  run -p <datei.zr>\n\n"
                    "Beispiel:\n"
                    "  run -p Skript.zr"
                )

            else:
                self._functions.ausgabe("Keine Argumente!", "r")
                print("Fuehre ?hilfe oder run -h aus wenn du hilfe brauchst")
                return

        elif cmd == "exit":
            print("Programm wird beendet.")
            sys.exit()

        elif cmd == ">":
            return

        elif cmd == "warte":
            try:
                if len(command_parts) < 2:
                    self._functions.wait(10, False)
                elif command_parts[1] == "-h":
                    print(
                        "Hilfe fuer warte\n"
                        "Verwendung:\n"
                        "  warte\n"
                        "  warte -t <sekunden>\n"
                        "  warte -t -ms_mode <millisekunden>\n\n"
                        "Beispiele:\n"
                        "  warte\n"
                        "  warte -t 2\n"
                        "  warte -t -ms_mode 500"
                    )
                elif command_parts[1] == "-t":
                    mi = True if command_parts[2] == "-ms_mode" else False

                    if len(command_parts) < 3 and (
                        True if not mi else False if len(command_parts) < 4 else True
                    ):
                        self._functions.ausgabe("Keine Argumente!", "r")
                        print("Fuehre ?hilfe oder warte -h aus wenn du hilfe brauchst")
                        return
                    elif int(command_parts[3] if mi else command_parts[2]) <= 0:
                        self._functions.ausgabe(
                            "Bitte gültige positive Ganzzahl eingeben!", "r"
                        )
                        print("Fuehre ?hilfe oder warte -h aus wenn du hilfe brauchst")
                        return

                    self._functions.wait(
                        int(command_parts[3] if mi else command_parts[2]), mi
                    )
                else:
                    self._functions.ausgabe("Falsche Argumente!", "r")
                    print("Fuehre ?hilfe oder warte -h aus wenn du hilfe brauchst")
                    return
            except IndexError:
                self._functions.ausgabe("Keine Argumente!", "r")
                print("Fuehre ?hilfe oder warte -h aus wenn du hilfe brauchst")
            except ValueError:
                self._functions.ausgabe("Bitte gültige positive Ganzzahl eingeben!", "r")
                print("Fuehre ?hilfe oder warte -h aus wenn du hilfe brauchst")

        else:
            print("Befehl nicht gefunden")
