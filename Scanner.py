import TokenType
import Token

class Scanner:
    def __init__(self, source):
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.source = source

    def scanTokens(self):
        while not self.isAtEnd():
            self.start = self.current
            self.scanToken()
            self.tokens.append(Token(TokenType.EOF,"", None, self.line))
            return self.tokens
    
    def scanToken(self):
        c = self.advance()
        if c ==  '(':
            self.addToken(TokenType.LEFT_PAREN);
        elif c ==  ')':
            self.addToken(TokenType.RIGHT_PAREN);
        elif c ==  '{':
            self.addToken(TokenType.LEFT_BRACE);
        elif c ==  '}':
            self.addToken(TokenType.RIGHT_BRACE);
        elif c ==  ',':
            self.addToken(TokenType.COMMA);
        elif c ==  '.':
            self.addToken(TokenType.DOT);
        elif c ==  '-':
            self.addToken(TokenType.MINUS);
        elif c ==  '+':
            self.addToken(TokenType.PLUS);
        elif c ==  ';':
            self.addToken(TokenType.SEMICOLON);
        elif c ==  '*':
            self.addToken(TokenType.STAR);
        elif c ==  '!':
            self.addToken(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG);
        elif c ==  '=':
            self.addToken(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL);
        elif c ==  '<':
            self.addToken(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS);
        elif c ==  '>':
            self.addToken(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER);
        elif c ==  '/':
            # Add handler
            pass
        elif c == '\r' or c == '\t' or c == ' ':
            pass
        elif c == '\n':
            self.line += 1
        elif c == '"':
            self.string()
        else:
            if (self.isDigit(c)):
                self.number()
            elif self.isAlpha(c):
                self.identifier()
            else:
                Main.error(self.line, "Unexpected Character")


    def advance(self):
        pass

    def identifier(self):
        while (self.isAlphaNumeric()):
            self.advance()
        text = self.source.substring(self.start, self.current)