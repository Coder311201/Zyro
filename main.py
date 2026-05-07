import sys
import interface
import functions

class main_app:
    def __init__(self):
        print('Gebe "?hilfe" oder ? ein wenn du hilfe brauchst')
        print("Copyright (C) 2026 Coder311201" \
        "Licensed under the GNU GPL v3")
        self.Interface = interface.Interface(False)

    def main(self):
        self.Interface.run()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        app = main_app()
        app.main()
    else:
        function = functions.functions(False)
        function.compile(sys.argv[1])
        sys.exit()
