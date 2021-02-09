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

    def assignvaralt(self, name, value, concat):
        self.variables[name] = ("%s %s" % (value,self.getvar(concat)))
    
    def getvar(self, name):
        return self.variables[name]

    def print_(self, param):
        print("%s" % self.cleanParam(param))

    def print_alt(self, param, concat):
        print("%s %s" % (self.cleanParam(param),self.getvar(concat)))
    
    def printvar(self, name):
        print("%s" % self.cleanParam((self.getvar(name))))

    def printvar_alt(self, name, concat):
        print("%s %s" % (self.cleanParam(self.getvar(name)),self.getvar(concat)))
    
    def docin(self,name):
        try:
            t = input()
            self.assignvar(name,t)
        except EOFError as e:
            pass

    def cleanParam(self, param):
        if re.match(r"^((\"[^\"]*\")|('[^']*'))$", param):
            return param[1:-1]
        return param

    def cleanParam_alt(self, param, concat):
        if re.match(r"^((\"[^\"]*\")|('[^']*'))$", param):
            return param[1:-1]
        return param