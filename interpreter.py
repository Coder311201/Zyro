import functions
import sys


class Interpreter:
    def __init__(self, debug: bool = True):
        self.functions = functions.functions(debug)
        self.vars = {}
        self.libs = {}
        if debug:
            print("Interpreter is running")

    def execute(self, command: str):
        if not "=>" in command.split():
            for var in self.vars:
                if var in command:
                    command = command.replace(var, str(self.vars.get(var, None)))

        command_parts = command.split()
        if not command_parts:
            return
        
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "^": lambda a, b: a ** b
        }
        p_ops = ["^", "*", "/"]
        o_ops = [item for item in ops if item not in p_ops]

        for ops_gr in [p_ops, o_ops]:
            for o in ops_gr:
                while True:
                    if o in command_parts:
                        o_i = command_parts.index(o)
                        if o_i < 1 or o_i >= len(command_parts) - 1:
                            self.functions.ausgabe("Fehler!", "r")
                            return
                        try:
                            x_1 = float(command_parts[o_i - 1].replace(",", "."))
                            x_2 = float(command_parts[o_i + 1].replace(",", "."))

                            x_e = ops[o](x_1, x_2)

                            if x_e.is_integer():
                                x_e = int(x_e)

                            x_e = str(x_e).replace(".", ",")

                            command_parts[o_i - 1:o_i + 2] = [x_e]

                        except ValueError:
                            self.functions.ausgabe("Fehler!", "r")
                            return
                        except ZeroDivisionError:
                            self.functions.ausgabe("Fehler!", "r")
                            print("Division durch null")
                            return
                    else: break
            

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
                "  Definiert eine Variable mit dem angegebenen Namen und Wert."
            )

        elif "=>" in command_parts:
            if command_parts.index("=>") != 0:
                var_name = " ".join(command_parts[: command_parts.index("=>")])
                var_value = " ".join(command_parts[command_parts.index("=>") + 1:])
                var_value = str(var_value)
                self.vars[var_name] = var_value
            else:
                self.functions.ausgabe("Ungültiger Variablename!", "r")

        elif cmd == "sage":
            if len(command_parts) < 2:
                self.functions.ausgabe("Keine Argumente!", "r")
                print("Fuehre ?hilfe oder sage -h aus wenn du hilfe brauchst")
                return
            if command_parts[1] == "-f":
                if len(command_parts) < 4:
                    self.functions.ausgabe("Keine Farbe oder Text!", "r")
                    print("Fuehre ?hilfe oder sage -h aus wenn du hilfe brauchst")
                    return
                text = " ".join(command_parts[3:])
                self.functions.ausgabe(text, command_parts[2])
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
                self.functions.ausgabe(text, "w")

        elif cmd == "run":
            if len(command_parts) < 2:
                self.functions.ausgabe("Keine Argumente!", "r")
                print("Fuehre ?hilfe oder run -h aus wenn du hilfe brauchst")
                return

            if command_parts[1] == "-p":
                if len(command_parts) < 3:
                    self.functions.ausgabe("Kein Pfad angegeben!", "r")
                    print("Fuehre ?hilfe oder run -h aus wenn du hilfe brauchst")
                    return
                self.functions.compile(command_parts[2])
            elif command_parts[1] == "-h":
                print(
                    "Hilfe fuer run\n"
                    "Verwendung:\n"
                    "  run -p <datei.zr>\n\n"
                    "Beispiel:\n"
                    "  run -p Skript.zr"
                )

            else:
                self.functions.ausgabe("Keine Argumente!", "r")
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
                    self.functions.wait(10, False)
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
                        self.functions.ausgabe("Keine Argumente!", "r")
                        print("Fuehre ?hilfe oder warte -h aus wenn du hilfe brauchst")
                        return
                    elif int(command_parts[3] if mi else command_parts[2]) <= 0:
                        self.functions.ausgabe(
                            "Bitte gültige positive Ganzzahl eingeben!", "r"
                        )
                        print("Fuehre ?hilfe oder warte -h aus wenn du hilfe brauchst")
                        return

                    self.functions.wait(
                        int(command_parts[3] if mi else command_parts[2]), mi
                    )
                else:
                    self.functions.ausgabe("Falsche Argumente!", "r")
                    print("Fuehre ?hilfe oder warte -h aus wenn du hilfe brauchst")
                    return
            except IndexError:
                self.functions.ausgabe("Keine Argumente!", "r")
                print("Fuehre ?hilfe oder warte -h aus wenn du hilfe brauchst")
            except ValueError:
                self.functions.ausgabe("Bitte gültige positive Ganzzahl eingeben!", "r")
                print("Fuehre ?hilfe oder warte -h aus wenn du hilfe brauchst")

        else:
            print("Befehl nicht gefunden")
