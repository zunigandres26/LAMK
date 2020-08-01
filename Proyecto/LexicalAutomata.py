# -*- coding: utf-8 -*-

from Token import Token

class LexicalAutomata:

    def __init__(self,reader):
        self.reader = reader

    def run(self):

        text = self.reader.text
        tokens = []

        i=0
        token = None
        while(i<len(text)):

            i,token = self.tokenCreator(text,i,token)
            if token.formed:
                tokens+= [token]

            self.tokens = tokens
        return self

    def tokenCreator(self,text,i,token=None):

        if not token or token.formed:
            token = Token()

        char, pos = ord(text[i]),i

        # Formar Números
        if (not token.inFormation and 
            self.isDigit(char)
        ):
            token.add(char)
            token.inFormation = True
            token.formed = False
            token.type = "Integer"

        elif token.inFormation:
                
            if (
                self.isDigit(char)
            ):
                token.add(char)
            elif (self.isDotOp(char)):
                token.add(char)
                token.type = "Float"
            else:
                token.formed = True

        else:

            token = Token()

        pos+=1
        return (pos,token)

    def isDigit(self,char):
        if (char>=48 and char <= 57):
            return True
        return False

    def isDotOp(self,char):
        return True if char==46 else False