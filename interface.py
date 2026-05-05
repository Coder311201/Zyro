import interpreter
import sys


class Interface:
    def __init__(self, debug: bool = True):
        self.executer = interpreter.Interpreter(debug)
        if debug:
            print("Interface is running")
            
    def run(self):
        print("Interface is started")
        try:
            while True:
                command = input(">> ")
                self.executer.execute(command)
        except KeyboardInterrupt:
            print("\nProgramm beendet")
            sys.exit()
