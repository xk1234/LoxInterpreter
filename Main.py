import TokenType
import Scanner
import Parser

class Main:
    hadError = False
    hadRuntimeError = False
    # interpreter = Interpreter()
    def __init__(self, args=[]):
        try:
            if len(args) == 1:
                Main.runFile(args[0])
            else:
                Main.runPrompt()
        except IOError as e:
            print("Error: " + str(e))
            exit(1)

    @staticmethod
    def runFile(path):
        pass

    @staticmethod
    def run(source):
        s = Scanner(source)
        tokens = s.scanTokens()
        p = Parser(tokens)

    @staticmethod
    def report(line, where, message):
        print(f"[line {line}] Error {where}: {message}")


    @staticmethod
    def error(token, message):
        if token == TokenType.EOF:
            pass

m = Main()