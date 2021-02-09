class Token:
    def __init__(self):
        self.formed = False
        self.inFormation = False
        self.value = []
        self.type = None

    def atFirst(self):
        if len(self.value) == 0: return None
        return self.value[0]

    def add(self,value):
        self.value += [value]

    def info(self):
        return ("".join(list(map(lambda x: chr(x),self.value))),self.type)

class Automata:
    def __init__(self,reader):
        self.reader = reader
    
    def run(self):
        text = self.reader.text
        tokens = []

        i = 0
        token = None
        while(i < len(text)):

            i,token = self.tokenCreator(text,i,token)
            if token.formed:
                tokens += [token]

        self.tokens = tokens
        return self

    def tokenCreator(self,text,i,token=None):
        #Para identificar Strings.
        if not token or token.formed:
            token = Token()
        char,pos = ord(text[i]),i
        if(not token.inFormation and self.is_number(char)):
            token.add(char)
            token.inFormation = True
            token.formed = False
            token.type = "Number"

        elif (token.inFormation):
            if(self.is_number(token.atFirst()) and self.is_number(char)):
                token.add(char)
            else:
                token.add(char)
                token.formed = True



        else:
            token = Token()
        pos += 1     
        return (pos,token)

    def is_quote(self,char):
        if (char == 34): return True
        return False

    def is_number(self,char):
        if char in range(48,58): return True
        return False