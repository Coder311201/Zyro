import sys
import interface
import functions

# Formatieren: black Zyro/
#KI: codex resume 019dee38-dbaa-7ea1-aba2-c0a5d68ecf4c


class main_app:
    def __init__(self):
        print('Gebe "?hilfe" oder ? ein wenn du hilfe brauchst')
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
