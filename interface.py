import interpreter
import sys


class Interface:
    def __init__(self, debug: bool = True):
        self.debug = debug
        self.executer = interpreter.Interpreter(debug)
        if self.debug:
            print("Interface is running")
            
    def run(self):
        if self.debug:
            print("Interface is started")
        try:
            while True:
                command = input(">> ")
                self.executer.execute(command)
        except KeyboardInterrupt:
            print("\nProgramm beendet")
            sys.exit()
