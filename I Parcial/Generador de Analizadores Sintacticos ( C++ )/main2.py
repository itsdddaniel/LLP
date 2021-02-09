from Reader import Reader
from Automata import Automata

reader = (Reader()).read()
automata = (Automata(reader)).run()


for token in automata.tokens:
    value, valueType = token.info()
    print(value)
    #print("\t%s - %s" % (value,valueType))