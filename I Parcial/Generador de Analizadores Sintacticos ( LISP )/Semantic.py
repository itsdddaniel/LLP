# -*- coding: utf-8 -*-
import re
from lark import Transformer, v_args

@v_args(inline=True)
class Semantic (Transformer):

    def __init__(self):
        self.variables = {}

    def sum (self, A, B):
        return float(A) + float(B)

    def sub (self, A, B):
        return float(A) - float(B)

    def multi(self,A,B):
        return (float(A)*float(B))

    def div(self,A,B):
        return (float(A)/float(B))
    
    def assignvar(self, name, value):
        self.variables[name] = value

    def assignvar_alt(self, name):
        print(name)
    
    def getvar(self, name):
        return self.variables[name]

    def printline(self, param):
        print("%s" % self.cleanParam(param))

    def printwrite(self, name):
        print(name)

    def cleanParam(self, param):
        if re.match(r"^((\"[^\"]*\")|('[^']*'))$", param):
            return param[1:-1]
        return param
