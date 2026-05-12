import math
import functions

class mathe:
    def __init__(self):
        self.functions = functions.functions(False)

    def pi(self):
        return math.pi
    
    def sin(self, x):
        try:
            x = float(x)
        except ValueError:
            self.functions.ausgabe("Fehler", "r")
            print("Bitte eine gültige Zahl übergeben")
            return
        y = math.sin(x)
        if y % 1 == 0: y = int(y)
        return y
    
    def cos(self, x):
        try:
            x = float(x)
        except ValueError:
            self.functions.ausgabe("Fehler", "r")
            print("Bitte eine gültige Zahl übergeben")
            return
        y = math.cos(x)
        if y % 1 == 0: y = int(y)
        return y
    
    def wurzel(self, x, We = 2):
        try:
            x = float(x)
        except ValueError:
            self.functions.ausgabe("Fehler", "r")
            print("Bitte eine gültige Zahl übergeben")
            return
        y = x ** (1 / We)
        if y % 1 == 0: y = int(y)
        return y