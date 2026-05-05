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
