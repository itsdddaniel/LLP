#-*- coding: utf-8 -*-
from plex.actions import TEXT, IGNORE, Begin
from plex.lexicons import Lexicon, State
from plex.regexps import RE, Seq, Alt, Rep1, Empty, Str, Any, AnyBut, AnyChar, Range
from plex.regexps import Opt, Rep, Bol, Eol, Eof, Case, NoCase
from plex.scanners import Scanner
from tabulate import tabulate
import sys

class LexicalAnalysis:
    def __init__(self):
        #Cadena de text
        letter = Range("AZaz")
        digits = Range("09")
        stringDouble = Str("\"") + Rep(AnyBut("\"")) + Str("\"")
        stringSimple =  Str("'") + Rep(AnyBut("'")) + Str("'")
        variable =  letter + Rep(letter | digits)

        space = Any(" \t\n")
        comment = Str("{") + Rep(AnyBut("{")) + Str("}")
        assignOP = Str("=")
        operators = Range("+-*/")

        self.lexicon = Lexicon(
            [
                (variable, "variable"),
                (stringDouble, "string"),
                (stringSimple, "string"),
                (digits, "number"),
                (operators,"operator"),
                (assignOP, "assign operator"),
                (space | comment,IGNORE)
            ]
        )
        #Str, Rep, AnyBut, Any
    
    def parse(self):
        lexicon = self.lexicon
        lexicalTable = []

        filename = sys.argv[1:][0]
        f = open(filename, "r")
        scanner = Scanner(lexicon, f, filename)

        while True:
            try:
                token = scanner.read()
                if not token[0]: break
                desc, val = token
                lexicalTable += [[val, desc]]

            except Exception as e:
                print ("Lexical Error: %s" % (e))
                f.close()
                return False

        f.close()
        self.lexicalTable = lexicalTable
        return self

parser = (LexicalAnalysis())

if parser.parse():
    print "Analisis Lexico: "
    print tabulate(parser.lexicalTable)