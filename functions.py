from colorama import Fore, Style, init
import os
import interpreter
import time


class functions:
    def __init__(self, debug: bool = True):
        init()        
        if debug:
            print("Functions loaded")

    def wait(self, w_time: int, ms_mode: bool):
        time.sleep(w_time if not ms_mode else w_time / 1000)

    def ausgabe(self, text: str, color: str):
        colors = {"r": "\033[31m", "g": "\033[32m", "b": "\033[34m"}
        if color not in colors and color != "w":
            self.ausgabe("Farbe nicht verfügbar", "r")
            print("Fuehre ?hilfe oder sage -h aus wenn du hilfe brauchst")
            return
        if color == "w":
            print(text)
        else:
            print(colors.get(color, "") + text + "\033[0m")

    def calculate(self, command_parts):
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "^": lambda a, b: a ** b
        }
        p_ops = ["^", "*", "/"]
        o_ops = [item for item in ops if item not in p_ops]

        while "(" in command_parts or ")" in command_parts:
            if ")" not in command_parts or "(" not in command_parts:
                self.ausgabe("Fehler!", "r")
                return None

            close_i = command_parts.index(")")
            open_i = None
            for i in range(close_i - 1, -1, -1):
                if command_parts[i] == "(":
                    open_i = i
                    break

            if open_i is None or open_i + 1 == close_i:
                self.ausgabe("Fehler!", "r")
                return None

            result = self.calculate(command_parts[open_i + 1:close_i])
            if result is None:
                return None
            command_parts[open_i:close_i + 1] = result

        for ops_gr in [p_ops, o_ops]:
            for o in ops_gr:
                while True:
                    if o in command_parts:
                        o_i = command_parts.index(o)
                        if o_i < 1 or o_i >= len(command_parts) - 1:
                            self.ausgabe("Fehler!", "r")
                            return None
                        try:
                            x_1 = float(command_parts[o_i - 1].replace(",", "."))
                            x_2 = float(command_parts[o_i + 1].replace(",", "."))

                            x_e = ops[o](x_1, x_2)

                            if x_e.is_integer():
                                x_e = int(x_e)

                            x_e = str(x_e).replace(".", ",")

                            command_parts[o_i - 1:o_i + 2] = [x_e]

                        except ValueError:
                            self.ausgabe("Fehler!", "r")
                            return None
                        except ZeroDivisionError:
                            self.ausgabe("Fehler!", "r")
                            print("Division durch null")
                            return None
                    else: break

        return command_parts

    def compile(self, dateipfad: str):

        if not os.path.exists(dateipfad):
            print("Datei existiert nicht!")
            return

        dateiendung = dateipfad.split(".")
        if not dateiendung[-1] == "zr":
            print("Falsche Datei!\n" 'Es werden nur ".zr" Datein unterstützt')
            return

        try:
            with open(dateipfad, "r", encoding="utf-8") as f:
                executer = interpreter.Interpreter(False)
                for zeile in f:
                    executer.execute(zeile)

        except Exception as e:
            print("Fehler beim Lesen:", e)
