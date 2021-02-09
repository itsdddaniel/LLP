"""
    ! Sintax Analysis
    ! Non-CFG
    * Permite

"""

import re
class SyntaxAnalysis:
    pass

    def __nit__(self): pass
    def help(self): pass
    def read(self):
        self.text = input()
        return self

    def parse(self): 
        text = self.text
        lines = re.split(r";",text)
        
        for i in range(len(lines)):
            line = ("%s".strip() % lines[i]).strip()
            if len(line) > 0:
                if(

                    re.match(r"^[A-Za-z][a-zA-z\d_]*\s*=\s*\d+(\.\d+)?$",line) or
                    re.match(r"^[A-Za-z][a-zA-z\d_]*\s*=\s*[A-Za-z][a-zA-z\d_]*$",line)

                ): pass
                else: quit("Error Sintactico: se ha encontrado un error en la linea %d" % i)
        return True

parser = (SyntaxAnalysis()).read()

if parser.parse():
    print("%s" % parser.text)