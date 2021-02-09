# -*- coding:utf-8 -*-

#sudo -Hpip3 install tabulate
from tabulate import tabulate
import sys,re

class InformalTokenParser:
    def __init__(self) : pass


    def read(self):
        #python3 lexicalAnalysis.py sample1.lng
        param = sys.argv[1:]
        if len(param) != 1: quit("Error. No se ha definido un programa a ejecutar.")
        self.fileName = param[0]
        f = open(self.fileName, "r")
        self.text = f.read() #Esta practica esta leyendo la completitud del programa.
        f.close()
        return self

    def preprocess(self):
        text = self.text
        text = re.sub(r"="," = ",text)
        text = re.sub(r";"," ; ",text)
        text = re.sub(r"\s+"," ",text)
        self.text = ("%s".strip() % text).strip()

        return self

    def lexicalAnalysis(self):
        result = []
        text = self.text
        tokens = re.split("\s",text)
        print(tokens)
        for token in tokens:
            token = ("%s".strip() % token).strip()
            if len(token) > 0:
                #Es un identificador de usuario
                if re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$",token):
                    result += [["Se reconoce el identificador de usuario","%s" % token]]

                #Es un operador de asignacion
                elif re.match(r"^=$",token):
                    result += [["Se reconoce el identificador de usuario","%s" % token]]

                #Es un numero flotante
                elif re.match(r"^\d+\.\d+$",token):
                    result += [["Se reconoce el identificador de usuario","%s" % token]]

                #
                elif re.match(r"^\d+$",token):
                    result += [["Se reconoce el identificador de usuario","%s" % token]]

                #
                elif re.match(r"^;$",token):
                    result += [["Se reconoce el identificador de usuario","%s" % token]]

                #
                else:
                    quit("Error: \n\tSe ha encontrado un token desconocido en la linea '%d': '%s'\n\n" % (self.searchTokenLine(token),token))
        return result
    
    def searchTokenLine(self,token):
        errorLine = 0
        f = open(self.fileName,"r")
        for line in f:
            errorLine += 1
            if re.match(r"^.*%s.*$" % self.prevent(token),line):
                break
        f.close()

        return errorLine

    def prevent(self,token):
        if re.match(r"[\+\.\(\)\{\}\[\]]",token):
            return "\\%s" % token
        return token

parser = (InformalTokenParser()).read().preprocess()


print("Programa Encontrado:")
print("\t%s\n" % parser.text)
print(parser.text)

lexicalAnalysis = parser.lexicalAnalysis()
print("El analisis lexico del software es: ")
print(tabulate(lexicalAnalysis))