#-*- coding: utf-8 -*-
import sys
from Reader import *
from Semantic import *
from lark import Lark, Transformer
from Grammar import *

reader = (Reader()).read()
parser = Lark(grammar,parser="lalr", transformer = Semantic())

language = parser.parse

sample = reader.text

try:
    language(sample)
except Exception as e:
    print("Error: %s" % e)