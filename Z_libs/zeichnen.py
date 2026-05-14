import turtle
import functions

class zeichnen:
    def __init__(self):
        self._s = turtle.Screen()
        self._s.title("Z Turtle")
        self._t = turtle.Turtle()
        self._functions = functions.functions(False)

    def vor(self, l: int):
        if l.isdigit():
            l = int(l)
        else:
            self._functions.ausgabe("Fehler")
            print("Bitte gültige Ganzzahl eingeben")
            return
        self._t.forward(int(l))
    
    def dreh_links(self, d: int):
        if d.isdigit():
            d = int(d)
        else:
            self._functions.ausgabe("Fehler")
            print("Bitte gültige Ganzzahl eingeben")
            return
        self._t.left(int(d))

    def dreh_rechts(self, d: int):
        if d.isdigit():
            d = int(d)
        else:
            self._functions.ausgabe("Fehler")
            print("Bitte gültige Ganzzahl eingeben")
            return
        self._t.right(int(d))

    def Titel(self, Titel: str):
        self._s.title(Titel)