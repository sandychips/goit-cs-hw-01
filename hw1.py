class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("Invalid character")

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def get_next_token(self):
        text = self.text

        if self.current_char is None:
            return Token(EOF, None)

        if self.current_char.isspace():
            self.advance()
            return self.get_next_token()

        if self.current_char.isdigit():
            token = Token(INTEGER, int(self.current_char))
            self.advance()
            return token

        if self.current_char == '+':
            self.advance()
            return Token(PLUS, '+')

        if self.current_char == '-':
            self.advance()
            return Token(MINUS, '-')

        if self.current_char == '*':
            self.advance()
            return Token(MUL, '*')

        if self.current_char == '/':
            self.advance()
            return Token(DIV, '/')

        if self.current_char == '(':
            self.advance()
            return Token(LPAREN, '(')

        if self.current_char == ')':
            self.advance()
            return Token(RPAREN, ')')

        self.error()

class Interpreter:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception("Invalid syntax")

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return token.value
        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()
            self.eat(RPAREN)
            return result

    def term(self):
        result = self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
                result *= self.factor()
            elif token.type == DIV:
                self.eat(DIV)
                result /= self.factor()

        return result

    def expr(self):
        result = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result += self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result -= self.term()

        return result

# Типи токенів
INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'LPAREN', 'RPAREN', 'EOF'

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

# Початковий вираз
text = "(3 + 4) * 5"

lexer = Lexer(text)
interpreter = Interpreter(lexer)
result = interpreter.expr()
print(result)
