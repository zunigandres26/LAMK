# -*- coding: utf-8 -*-

import re

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
        if (str(type(value))=="<class 'lark.tree.Tree'>"):
            self.variables[name] = value.data
        else:
            self.variables[name] = value

    def getvar(self,name):
        return self.variables[name]

    def forfunction(self, name, value,condition,unary, *args):
        
        self.assignvar(name,value)
        condition = self.getValues(condition," ")
        unary = self.getUnary(self.getValues(unary," ")[-1].strip())
        statements = [
                        self.cleanDeclaration (
                            self.getValues(x,"#INDENT#") 
                        )
                        for x in args
                    ]

        print( statements )

        if ((name == condition[1] or name == condition[3]) and 
            (condition[1] != condition[3])
        ):
            start = int(value)
            end = self.getEnd(condition,name)

            # for (int i=0; i<10; i++)
            # for (int i=10; i>0; i--)
            # for (int i=0; 10>i; i++)
            # for (int i=10; 0<i; i--)
            if ((condition[1]==name and condition[2]=="<" and unary==1) or
                (condition[1]==name and condition[2]==">" and unary== -1) or 
                (condition[3]==name and condition[2]=="<" and unary== -1) or 
                (condition[3]==name and condition[2]==">" and unary== 1)
            ):
                self.repeatStatements(start,end,unary,statements)
            
            # for (int i=0; i<=30; i++)
            # for (int i=0; 30>=i; i++)
            elif ((condition[1]==name and condition[2]=="<=" and unary== 1) or
                (condition[3]==name and condition[2]==">=" and unary == 1)
            ):
                self.repeatStatements(start,end+1,unary,statements)

            # for (int i=30; i>=0; i--)
            # for (int i=30; 0<=i; i--)
            elif ((condition[1]==name and condition[2]==">=" and unary== -1) or
                (condition[3]==name and condition[2]=="<=" and unary== -1)
            ):
                self.repeatStatements(start+1,end,unary,statements)

    
            
    def repeatStatements(self,start,end,unary,statements):           
        for i in range(start,end,unary):
            operation = self.assignOperation( statements[i] )
            print( operation )
            for statement in statements:
                if statement[1]=="log":
                    self.printlog(statement[-1])
                elif statement[1] == "error":
                    self.printlog(statement[-1])

    def assignOperation(self,  statements): 
        return self.evalFunctionOperation( statements )  if "operation" in statements else 0

    def getUnary(self,unary):
        return 1 if unary=="++" else -1

    def getEnd (self,condition,name):
        end = 0
        if (re.match(r"\d+",condition[1])):
            end = int(condition[1])
        elif (re.match(r"\d+",condition[3])):
            end = int(condition[3])
        elif (re.match(r"%s" % name,condition[1])):
            end = self.getvar(condition[3])
        else:
            end = self.getvar(condition[1])
        return end

    def getValues (self,tree,indent):
        tree = tree.pretty(indent_str=indent).split(indent)
        tree = [x.strip() for x in tree]
        return tree

    # Limpia un arreglo sustraido del árbol de Lark
    def cleanDeclaration(self, arrayVarStatement ):
        if 'operation' in arrayVarStatement: 
            return self.cleanVarStatementDeclaration( arrayVarStatement )
        else: 
            return self.cleanForStatement( arrayVarStatement )

    # Limpia el arreglo que contiene las operaciones 
    # aritméticas
    def cleanVarStatementDeclaration(self, arrayVarStatement ): 
        newStatement =[]
        for statement in arrayVarStatement: 
            if statement != "operation" and statement != "":
                if re.search(r"\t", statement):
                    newStatement.append( statement[-1] )
                else:
                    newStatement.append( statement )
        varStatement = arrayVarStatement[0:3]
        op = newStatement[2:]
        return varStatement + op

    # true\ttrue --> true
    def cleanForStatement(self, arrayVarStatement ): 
        newStatement =[]
        for statement in arrayVarStatement: 
            if re.search(r"\t", statement):
                newStatement.append( re.split(r"\t", statement)[-1] )
            else: 
                newStatement.append( statement )
        return newStatement

    # Evalua operaciones matemáticas
    def evalFunctionOperation(self, arrayVarStatement):
        op = arrayVarStatement[3:]
        strOp = "".join( op )
        
        if re.search(r"[a-zA-Z]", strOp): 
            for i in range(len(op)): 
                if re.search(r"[a-zA-Z]+", op[i]): 
                    op[i] = self.getvar( op[i] )
            return eval( "".join( op ) )        
        else: 
            return eval( strOp )
