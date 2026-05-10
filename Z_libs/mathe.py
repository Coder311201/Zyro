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
        return y
    
    def cos(self, x):
        try:
            x = float(x)
        except ValueError:
            self.functions.ausgabe("Fehler", "r")
            print("Bitte eine gültige Zahl übergeben")
            return
        y = math.cos(x)
        return y