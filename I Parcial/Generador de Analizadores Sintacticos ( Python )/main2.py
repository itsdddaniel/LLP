# -*- coding: utf-8 -*-
from FSM import FiniteStateMachine
from tabulate import tabulate
import sys

class CAutomata:
    def __init__(self): pass

    def message(self):    
        print("")
        print("*"*80)
        print("*"*80)
        print(
            """
                            Python Automata
            ----------------------------------------------------
            Permite que el usuario lea un archivo de C++ 
            y sea reconocido como lenguaje C++ por su lexico
            @author Daniel Arteaga
            @date 2020/07/17
            @version 0.1
                """
            )
        print("*"*80)
        print("*"*80)
        print("")

    def load(self):
        param = sys.argv[1:]
        if len(param) != 1: quit("Error. No se ha definido un programa a ejecutar.")
        self.fileName = param[0]
        f = open(self.fileName, "r")
        self.text = f.read()
        f.close()
        return self

    def preprocess(self):
        self.text = ("%s".strip() % self.text).strip()
        result = ' '.join(self.text.split())
        self.text = result
        return self

    def run(self):
        text =  self.text
        FSM = FiniteStateMachine()
        FSM.startFSM()
        return FSM.runFSM(text)

(CAutomata()).message()
run = (CAutomata()).load().preprocess().run()

headers = ["Description","Index","Token","Symbol"]
print("\n")
print("\nEl resultado es:\n")
print("%s"%tabulate(run,headers,tablefmt="psql"))