# -*- coding: utf-8 -*-

class Automata:
    def __init__(self): pass

    def message(self):

        print("")
        print("*"*80)
        print("*"*80)
        print(
                """
                                  String Automata
                -----------------------------------------------------
                Permite que el usuario ingrese una cadena(strings) 
                y sean reconocidos mediante comillas simples o dobles
                @author Daniel Arteaga
                @date 2020/07/15
                @version 0.1
                """
            )
        print("*"*80)
        print("*"*80)
        print("Expresion regular equivalente: \"([^\\\"]|\\.)*\" ")
        print("")

    def load(self,text=input("Ingrese una palabra o frase: ")):
        self.text = text
        return self

    def stringAutomata(self):
        result = []
        one = "'"
        two = '"'
        text = self.text
        for i in range(len(text)):
            if len(text) > 0:
                if (one in text):
                    result = text.split(" ")
                elif (one not in text):
                    pass
                if (two in text):
                    result = text.split(' ')
                elif (two not in text):
                    pass
            else:
                return "Cadena vacia."
        return result

run = (Automata()).load().stringAutomata()
(Automata()).message()
print(run)

