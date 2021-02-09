from tabulate import tabulate
import sys, re

class SemanticAnalysis:

    def __init__(self): pass
    def help(self): pass

    def clean(self,text):
        return ("%s".strip() % text).strip()

    def read(self):
        try:
            text = input()
            while True:
                self.text += [text]
                text = input()
        except EOFError:
            pass

    def splitInstruction(self,line):
        var,val = re.split(r"=",line)
        var = self.clean(var)
        val = self.clean(val)
        return (var,val)

    def UDV(self): 
        result = {}
        text = self.text
        lines = re.split(r";",text)

        for i in range(len(lines)):

            line = self.clean(lines[i])
            if len(line)>0:

                if re.match(r"^[A-Za-z][a-zA-z\d_]*\s*=\s*\d+$",line):
                    var,val = self.splitInstruction(line)
                    result[var] = {"type":"int","value":val} 

                elif re.match(r"^[A-Za-z][a-zA-z\d_]*\s*=\s*\d+(\.\d+)?$",line):
                    var,val = self.splitInstruction(line)
                    result[var] = {"type":"float","value":val}

                elif re.match(r"^[A-Za-z][a-zA-z\d_]*\s*=\s*[A-Za-z][a-zA-z\d_]*$",line):
                    var,val = self.splitInstruction(line)
                    variables = result.keys()
                    if val not in variables:
                        quit("Error semantico: no existe la variable o asignacion '%s'." % val)
                    
                    result[var] = {"type":result[val]["type"],"value":val}

                else:
                    quit("Error Semantico: no se ha encontrado la definicion '%s'." % line)
                

        return result

    def jsonToMatrix(self,json): 
        result = []
        header = []
        count = 0
        for k,v in json.items():
            row = [k]
            for k1,v1 in v.items():
                count+=1
                if count<3:
                    header += [self.clean(k1)]
                row += [v1]
            result += [row]
        return [["Name"]+header] + [["-"*5,"-"*5,"-"*5]] + result

parser = (SemanticAnalysis()).read()
UDV = (SemanticAnalysis()).UDV()
print(tabulate(parser.jsonToMatrix(UDV)))