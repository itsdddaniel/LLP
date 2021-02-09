# -*- coding: utf-8 -*-

class FiniteStateMachine:
    def __init__(self):
        self.currentState = None
        self.current = ""
        #------------------------------------------------------------
        self.digits = ["0","1","2","3","4","5","6","7","8","9"]
        self.alphabet =  [
                        "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                    ]
        self.blankspaces = [" ", "\n"]
        self.assingment = ["="]
        self.operators = ["+","-","*","/","==",">","<"]
        self.increment_decrement = ["++","--"]
        self.finalInstruction = [";"]
        self.alphanumeric = ["_"]
        self.alphanumeric += self.digits + self.alphabet
        self.punctuation = [".",","]
        self.others = ["#"]
        self.scope = ["::",":"]
        self.instructions = ["(",")","{","}","|",'"']
        self.bitwiseshift = [">>","<<"]
        #------------------------------------------------------------
        self.successStates = ["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"]
        self.reservedStates = ""
        self.endState = ["A13"]
        self.exitState = ["A14"]
        self.startState = ["A0"]

    def startFSM(self):
        print("-"*80)
        print("\nLa FSM ha comenzado. \n")
        print("-"*80)
        self.changeFSM("A0",'')


    def changeFSM(self,state,cs):
        if state in self.startState:
            print("Se mueve al estado de inicio: %s"%(state))
            self.current = state
        
        elif state in self.exitState:
            print("Se ha finalizado el FSM con estado de fin: %s"%(state))

        elif state in self.successStates:
            self.current = state
            print("Se termino existosamente por lo que se mueve al estado de exito: '%s'"%(state))

        elif state in self.reservedStates:
            self.current = state
            print("Se mueve al estado: '%s' con el caracter '%s'"%(state,cs))

    def runFSM(self,text):
        result = []
        increment = 0
        text = text.replace("\\n", "\n")
        for i in range(len(text)):
            
            count = 1
            if text[i] in self.assingment:
                temp = 0
                if text[i] == "=":
                    temp += 1
                    if(text[i+temp] != "="):
                        self.reservedStates = "C""%s" % increment
                        result +=   [["Assignment at index: ","%s" % i,"ASSINGMENT","%s" % text[i]]]
                        self.changeFSM(self.reservedStates,text[i+temp])
                        temp += 1
                    
                    elif(text[i+temp] is "="):
                        self.reservedStates = "O""%s" % increment
                        result += [["Operator at index: ","%s" % i,"OPERATOR","%s" % text[i]+text[i+temp]]]
                        self.changeFSM(self.reservedStates,text[i+temp])
        
            elif text[i] in self.alphanumeric:
                result += [["Letter at: ","%s" % i,"IDENTIFER","%s" % text[i]]]

            elif text[i] in self.finalInstruction:
                result += [["End Instruction at: ","%s" % i,"END_INSTRUCTION","%s" % text[i]]]
                self.changeFSM("A3",text[i])

            elif text[i] in self.punctuation:
                result += [["Punctuation at: ","%s" % i,"PUNCTUATION","%s" % text[i]]]
                self.changeFSM("A4",text[i])

            elif text[i] in self.others:
                self.changeFSM(self.reservedStates,text[i])
                if text[i+count] == "e":
                    self.reservedStates = "B""%s" % increment
                    self.changeFSM(self.reservedStates,text[i+count])
                    count += 1
                    if(text[i+count] == "n"):
                        self.reservedStates = "B""%s" % increment
                        self.changeFSM(self.reservedStates,text[i+count])
                        count += 1
                        if(text[i+count] == "d"):
                            self.reservedStates = "B""%s" % increment
                            self.changeFSM(self.reservedStates,text[i+count])
                            count += 1
                            if(text[i+count] == "i"):
                                self.reservedStates = "B""%s" % increment
                                self.changeFSM(self.reservedStates,text[i+count])
                                count += 1
                                if(text[i+count] == "f"):
                                    self.reservedStates = "B""%s" % increment
                                    result +=   [
                                                    ["Reserved Word at index: ","%s" % i,"OTHER: ","%s" % text[i]]
                                                ]
                                    self.changeFSM(self.reservedStates,text[i+count])

                elif text[i+count] == "i" and text[i+2] == "n":
                    self.reservedStates = "B""%s" % increment
                    self.changeFSM(self.reservedStates,text[i+count])
                    count += 1
                    if(text[i+count] == "n"):
                        self.reservedStates = "B""%s" % increment
                        self.changeFSM(self.reservedStates,text[i+count])
                        count += 1
                        if(text[i+count] == "c"):
                            self.reservedStates = "B""%s" % increment
                            self.changeFSM(self.reservedStates,text[i+count])
                            count += 1
                            if(text[i+count] == "l"):
                                self.reservedStates = "B""%s" % increment
                                self.changeFSM(self.reservedStates,text[i+count])
                                count += 1
                                if(text[i+count] == "u"):
                                    self.reservedStates = "B""%s" % increment
                                    self.changeFSM(self.reservedStates,text[i+count])
                                    count += 1
                                    if(text[i+count] == "d"):
                                        self.reservedStates = "B""%s" % increment
                                        self.changeFSM(self.reservedStates,text[i+count])
                                        count += 1
                                        if(text[i+count] == "e"):
                                            self.reservedStates = "R""%s" % increment
                                            result +=   [
                                                            ["Reserved Word at index: ","%s" % i,"OTHER","%s" % text[i]]
                                                        ]
                                            self.changeFSM(self.reservedStates,text[i+count])

                elif text[i+count] == "i" and text[i+2] == "f":
                    self.reservedStates = "B""%s" % increment
                    self.changeFSM(self.reservedStates,text[i+count])
                    count += 1
                    if(text[i+count] == "f"):
                        self.reservedStates = "B""%s" % increment
                        self.changeFSM(self.reservedStates,text[i+count])
                        count += 1
                        if(text[i+count] == "n"):
                            self.reservedStates = "B""%s" % increment
                            self.changeFSM(self.reservedStates,text[i+count])
                            count += 1
                            if(text[i+count] == "d"):
                                self.reservedStates = "B""%s" % increment
                                self.changeFSM(self.reservedStates,text[i+count])
                                count += 1
                                if(text[i+count] == "e"):
                                    self.reservedStates = "B""%s" % increment
                                    self.changeFSM(self.reservedStates,text[i+count])
                                    count += 1
                                    if(text[i+count] == "f"):
                                        self.reservedStates = "B""%s" % increment
                                        result +=   [
                                                            ["Reserved Word at index: ","%s" % i,"OTHER","%s" % text[i]]
                                                        ]
                                        self.changeFSM(self.reservedStates,text[i+count])

                elif text[i+count] == "d":
                    self.reservedStates = "B""%s" % increment
                    self.changeFSM(self.reservedStates,text[i+count])
                    count += 1
                    if(text[i+count] == "e"):
                        self.reservedStates = "B""%s" % increment
                        self.changeFSM(self.reservedStates,text[i+count])
                        count += 1
                        if(text[i+count] == "f"):
                            self.reservedStates = "B""%s" % increment
                            self.changeFSM(self.reservedStates,text[i+count])
                            count += 1
                            if(text[i+count] == "i"):
                                self.reservedStates = "B""%s" % increment
                                self.changeFSM(self.reservedStates,text[i+count])
                                count += 1
                                if(text[i+count] == "n"):
                                    self.reservedStates = "B""%s" % increment
                                    self.changeFSM(self.reservedStates,text[i+count])
                                    count += 1
                                    if(text[i+count] == "e"):
                                        self.reservedStates = "R""%s" % increment
                                        result +=   [["Reserved Word at index: ","%s" % i,"OTHER","%s" % text[i]]]
                                        self.changeFSM(self.reservedStates,text[i+count])
                                            
                
            elif text[i] in self.blankspaces:
                temporal = 1
                if text[i+temporal] == "c":
                    self.reservedStates = "R""%s" % increment
                    self.changeFSM(self.reservedStates,text[i+temporal])
                    temporal += 1
                    if(text[i+temporal] == "l"):
                        self.reservedStates = "R""%s" % increment
                        self.changeFSM(self.reservedStates,text[i+temporal])
                        temporal += 1
                        if(text[i+temporal] == "a"):
                            self.reservedStates = "R""%s" % increment
                            self.changeFSM(self.reservedStates,text[i+temporal])
                            temporal += 1
                            if(text[i+temporal] == "s"):
                                self.reservedStates = "R""%s" % increment
                                self.changeFSM(self.reservedStates,text[i+temporal])
                                temporal += 1
                                if(text[i+temporal] == "s"):
                                    self.reservedStates = "R""%s" % increment
                                    result += [["Reserved Word at index: ","%s" % i,"BLANKSPACES","%s" % text[i]]]
                                    self.changeFSM(self.reservedStates,text[i+temporal])
                                    
                elif text[i+temporal] == "f":
                    self.reservedStates = "R""%s" % increment
                    self.changeFSM(self.reservedStates,text[i+temporal])
                    temporal += 1
                    if text[i+temporal] == "l":
                        self.reservedStates = "R""%s" % increment
                        self.changeFSM(self.reservedStates,text[i+temporal])
                        temporal += 1
                        if text[i+temporal] == "o":
                            self.reservedStates = "R""%s" % increment
                            self.changeFSM(self.reservedStates,text[i+temporal])
                            temporal += 1
                            if text[i+temporal] == "a":
                                self.reservedStates = "R""%s" % increment
                                self.changeFSM(self.reservedStates,text[i+temporal])
                                temporal += 1
                                if text[i+temporal] == "t":
                                    self.reservedStates = "R""%s" % increment
                                    result += [["Reserved Word at index: ","%s" % i,"BLANKSPACES","%s" % text[i]]]
                                    self.changeFSM(self.reservedStates,text[i+temporal])

                elif text[i+temporal] == "p":
                    self.reservedStates = "R""%s" % increment
                    self.changeFSM(self.reservedStates,text[i+temporal])
                    temporal += 1
                    if text[i+temporal] == "u":
                        self.reservedStates = "R""%s" % increment
                        self.changeFSM(self.reservedStates,text[i+temporal])
                        temporal += 1
                        if text[i+temporal] == "b":
                            self.reservedStates = "R""%s" % increment
                            self.changeFSM(self.reservedStates,text[i+temporal])
                            temporal += 1
                            if text[i+temporal] == "l":
                                self.reservedStates = "R""%s" % increment
                                self.changeFSM(self.reservedStates,text[i+temporal])
                                temporal += 1
                                if text[i+temporal] == "i":
                                    self.reservedStates = "R""%s" % increment
                                    self.changeFSM(self.reservedStates,text[i+temporal])
                                    temporal += 1
                                    if text[i+temporal] == "c":
                                        self.reservedStates = "R""%s" % increment
                                        result += [["Reserved Word at index: ","%s" % i,"BLANKSPACES","%s" % text[i]]]
                                        self.changeFSM(self.reservedStates,text[i+temporal])

                elif text[i+temporal] == "r":
                    self.reservedStates = "R""%s" % increment
                    self.changeFSM(self.reservedStates,text[i+temporal])
                    temporal += 1   
                    if text[i+temporal] == "e":
                        self.reservedStates = "R""%s" % increment
                        self.changeFSM(self.reservedStates,text[i+temporal])
                        temporal += 1   
                        if text[i+temporal] == "t":
                            self.reservedStates = "R""%s" % increment
                            self.changeFSM(self.reservedStates,text[i+temporal])
                            temporal += 1   
                            if text[i+temporal] == "u":
                                self.reservedStates = "R""%s" % increment
                                self.changeFSM(self.reservedStates,text[i+temporal])
                                temporal += 1 
                                if text[i+temporal] == "r":
                                    self.reservedStates = "R""%s" % increment
                                    self.changeFSM(self.reservedStates,text[i+temporal])
                                    temporal += 1 
                                    if text[i+temporal] == "n":
                                        self.reservedStates = "R""%s" % increment
                                        result += [["Reserved Word at index: ","%s" % i,"BLANKSPACES","%s" % text[i]]]
                                        self.changeFSM(self.reservedStates,text[i+temporal])

                elif text[i+temporal] == "m":
                    self.reservedStates = "R""%s" % increment
                    self.changeFSM(self.reservedStates,text[i+temporal])
                    temporal += 1 
                    if text[i+temporal] == "a":
                        self.reservedStates = "R""%s" % increment
                        self.changeFSM(self.reservedStates,text[i+temporal])
                        temporal += 1
                        if text[i+temporal] == "i":
                            self.reservedStates = "R""%s" % increment
                            self.changeFSM(self.reservedStates,text[i+temporal])
                            temporal += 1 
                            if text[i+temporal] == "n":
                                self.reservedStates = "R""%s" % increment
                                result += [["Reserved Word at index: ","%s" % i,"BLANKSPACES","%s" % text[i]]]
                                self.changeFSM(self.reservedStates,text[i+temporal])

                elif text[i+temporal] == "s":
                    self.reservedStates = "R""%s" % increment
                    self.changeFSM(self.reservedStates,text[i+temporal])
                    temporal += 1 
                    if text[i+temporal] == "t":
                        self.reservedStates = "R""%s" % increment
                        self.changeFSM(self.reservedStates,text[i+temporal])
                        temporal += 1 
                        if text[i+temporal] == "d":
                            self.reservedStates = "R""%s" % increment
                            result += [["Reserved Word at index: ","%s" % i,"BLANKSPACES","%s" % text[i]]]
                            self.changeFSM(self.reservedStates,text[i+temporal])

                elif text[i+temporal] == "c":
                    self.reservedStates = "R""%s" % increment
                    self.changeFSM(self.reservedStates,text[i+temporal])
                    temporal += 1 
                    if text[i+temporal] == "i":
                        self.reservedStates = "R""%s" % increment
                        self.changeFSM(self.reservedStates,text[i+temporal])
                        temporal += 1 
                        if text[i+temporal] == "n":
                            self.reservedStates = "R""%s" % increment
                            result += [["Reserved Word at index: ","%s" % i,"BLANKSPACES","%s" % text[i]]]
                            self.changeFSM(self.reservedStates,text[i+temporal])

                elif text[i+temporal] == "c":
                    self.reservedStates = "R""%s" % increment
                    self.changeFSM(self.reservedStates,text[i+temporal])
                    temporal += 1
                    if text[i+temporal] == "o":
                        self.reservedStates = "R""%s" % increment
                        self.changeFSM(self.reservedStates,text[i+temporal])
                        temporal += 1    
                        if text[i+temporal] == "u":
                            self.reservedStates = "R""%s" % increment
                            self.changeFSM(self.reservedStates,text[i+temporal])
                            temporal += 1 
                            if text[i+temporal] == "t":
                                self.reservedStates = "R""%s" % increment
                                result += [["Reserved Word at index: ","%s" % i,"BLANKSPACES","%s" % text[i]]]
                                self.changeFSM(self.reservedStates,text[i+temporal])  
                else:
                    result += [["-"*20,"%s" % i,"-"*20,"%s" % text[i]]]
                    

            elif text[i] in self.instructions:
                if text[i] == "(":  
                    self.reservedStates = "F""%s" % increment
                    result += [["Function Instruction at index: ","%s" % i,"FUNCTION_INSTRUCTION","%s" % text[i]]]
                    self.changeFSM(self.reservedStates,text[i])

                elif text[i] == ")":
                    self.reservedStates = "F""%s" % increment
                    result += [["Function Instruction at index: ","%s" % i,"FUNCTION_INSTRUCTION","%s" % text[i]]]
                    self.changeFSM(self.reservedStates,text[i])

                elif text[i] == "{":
                    self.reservedStates = "F""%s" % increment
                    result += [["Function Instruction at index: ","%s" % i,"FUNCTION_INSTRUCTION","%s" % text[i]]]
                    self.changeFSM(self.reservedStates,text[i])

                elif text[i] == "}":
                    self.reservedStates = "F""%s" % increment
                    result += [["Function Instruction at index: ","%s" % i,"FUNCTION_INSTRUCTION","%s" % text[i]]]
                    self.changeFSM(self.reservedStates,text[i])

                elif text[i] == "|":
                    self.reservedStates = "F""%s" % increment
                    result += [["Function Instruction at index: ","%s" % i,"FUNCTION_INSTRUCTION","%s" % text[i]]]
                    self.changeFSM(self.reservedStates,text[i])

                elif text[i] == '"':
                    self.reservedStates = "F""%s" % increment
                    result += [["Function Instruction at index: ","%s" % i,"FUNCTION_INSTRUCTION","%s" % text[i]]]
                    self.changeFSM(self.reservedStates,text[i])

            elif text[i] in self.operators:

                temp = 0
                if text[i] == "+":
                    temp += 1
                    if(text[i+temp] != "+"):
                        self.reservedStates = "O""%s" % increment
                        result += [["Operator at index: ","%s" % i,"OPERATOR","%s" % text[i]]]
                        self.changeFSM(self.reservedStates,text[i+temp])
                    
                    elif(text[i+temp] is "+"):
                        self.reservedStates = "ID""%s" % increment
                        result += [["Increment at index: ","%s" % i,"INCREMENT_DECREMENT","%s" % text[i]+text[i+temp]]]
                        self.changeFSM(self.reservedStates,text[i+temp])
                        temp += 1

                if text[i] == "-":
                    temp += 1
                    if(text[i+temp] != "-"):
                        self.reservedStates = "O""%s" % increment
                        result += [["Operator at index: ","%s" % i,"OPERATOR","%s" % text[i]]]
                        self.changeFSM(self.reservedStates,text[i+temp])
                    
                    elif(text[i+temp] is "-"):
                        self.reservedStates = "ID""%s" % increment
                        result += [["Decrement at index: ","%s" % i,"INCREMENT_DECREMENT","%s" % text[i]+text[i+temp]]]
                        self.changeFSM(self.reservedStates,text[i+temp])
                        temp += 1

                if text[i] == ">":
                    temp += 1
                    if(text[i+temp] != ">"):
                        self.reservedStates = "O""%s" % increment
                        result += [["Operator at index: ","%s" % i,"OPERATOR","%s" % text[i]]]
                        self.changeFSM(self.reservedStates,text[i+temp])
                    
                    elif(text[i+temp] is ">"):
                        self.reservedStates = "ID""%s" % increment
                        result += [["Bitwiseshift at index: ","%s" % i,"Bitwiseshift","%s" % text[i]+text[i+temp]]]
                        self.changeFSM(self.reservedStates,text[i+temp])
                        temp += 1

                if text[i] == "<":
                    temp += 1
                    if(text[i+temp] != "<"):
                        self.reservedStates = "O""%s" % increment
                        result += [["Operator at index: ","%s" % i,"OPERATOR","%s" % text[i]]]
                        self.changeFSM(self.reservedStates,text[i+temp])
                    
                    elif(text[i+temp] is "<"):
                        self.reservedStates = "ID""%s" % increment
                        result += [["Bitwiseshift at index: ","%s" % i,"Bitwiseshift","%s" % text[i]+text[i+temp]]]
                        self.changeFSM(self.reservedStates,text[i+temp])
                        temp += 1

                elif (text[i] == "/"):
                    self.reservedStates = "O""%s" % increment
                    result += [["Operator at index: ","%s" % i,"OPERATOR","%s" % text[i]]]
                    self.changeFSM(self.reservedStates,text[i])
                    count += 1

                elif (text[i] == "*"):
                    self.reservedStates = "O""%s" % increment
                    result += [["Operator at index: ","%s" % i,"OPERATOR","%s" % text[i]]]
                    self.changeFSM(self.reservedStates,text[i])
                    count += 1

            elif text[i] in self.scope:
                if (text[i] and text[i+1]) == ":":
                    self.reservedStates = "F""%s" % increment
                    result += [["Scope at index: ","%s" % i,"SCOPE","%s" % text[i]]]
                    self.changeFSM(self.reservedStates,text[i])

            else:
                result += [["Unknown Token at: ","%s" % i,"UNKNOWN","%s" % text[i]]]
                self.changeFSM("A13",text[i])

            increment += 1
        return result