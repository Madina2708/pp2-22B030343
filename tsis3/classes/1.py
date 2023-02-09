class InputOutString():
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = input()

    def print_String(self):
        print(self.s.upper())

s = InputOutString()
s.get_String()
s.print_String()