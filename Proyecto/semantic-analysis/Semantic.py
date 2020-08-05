# -*- coding: utf-8 -*-

import re
from lark import Transformer, v_args, Tree

@v_args(inline=True)
class Semantic(Transformer):

    def __init__(self):
        self.variables = {}

    def printlog (self,text):
        print("\033[0;32m%s" % text)

    def printerror (self,text):
        print("\033[0;1;31m%s" % text)

    def printvarlog (self,var):
        self.printlog(self.getvar(var))

    def printvarerror (self,var):
        self.printerror (self.getvar(var))

    def sum(self, A, B):
        if (isinstance(A,int) and isinstance(B,int)):
            return int(A)+int(B)
        else:
            return float(A)+float(B)

    def sub(self,A,B):
        if (isinstance(A,int) and isinstance(B,int)):
            return int(A)-int(B)
        else:
            return float(A)-float(B)

    def mul(self,A,B):
        if (isinstance(A,int) and isinstance(B,int)):
            return int(A)*int(B)
        else:
            return float(A)*float(B)

    def div(self,A,B):
        if int(B) is not 0:
            if (isinstance(A,int) and isinstance(B,int)):
                return int(A)/int(B)
            else:
                return float(A)/float(B)
        else:
            self.printerror("Infinito chaval, como el universo")

    def assignvar(self,name,value):
        self.variables[name] = value

    def getvar(self,name):
        return self.variables[name]

    def forfunction(self, name, value,condition,unary, *args):
        
        condition = self.getValues(condition," ")
        unary = self.getUnary(self.getValues(unary," ")[-1].strip())
        statements = [self.getValues(x,"#INDENT#") for x in args]
        start = int(value)
        end = self.getEnd(condition)
        """
        if ((name == condition[1] or name == condition[3]) and 
            (condition[1] not condition[3]) and
            (name == unary[1])
        ):
            start = int(value)
            end = self.getEnd(condition)

            for i in statements:
        """
        for i in range (start,end,unary):
            for statement in statements:
                if (statement[1]=="log"):
                    self.printlog(statement[-1])
                elif (statement[1]=="error"):
                    self.printerror(statement[-1])

    def getUnary(self,unary):
        return 1 if unary=="++" else -1

    def getEnd (self,condition):
        end = 0
        if (re.match(r"\d+",condition[1])):
            end = int(condition[1])
        elif (re.match(r"\d+",condition[3])):
            end = int(condition[3])
        elif (re.match(r"%" % name,condition[1])):
            end = self.getvar(condition[3])
        else:
            end = self.getvar(condition[1])
        return end

    def getValues (self,tree,indent):
        tree = tree.pretty(indent_str=indent).split(indent)
        tree = [x.strip() for x in tree]
        return tree