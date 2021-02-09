#-*- coding: utf-8 -*-
class Reader:

    def __init__(self): pass

    def read(self):
        self.text = []

        try:
            text = input()
            while True:
                self.text += [text]
                text = input()
        except EOFError:
            pass
        self.text = "\n".join(self.text)
        return self