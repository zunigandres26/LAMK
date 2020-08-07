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
            self.variables[str(name)] = value.data
        else:
            self.variables[str(name)] = value

    def getvar(self,name):
        return self.variables[str(name)]

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
                self.repeatStatements(name,start,end,unary,statements)
            
            # for (int i=0; i<=30; i++)
            # for (int i=0; 30>=i; i++)
            elif ((condition[1]==name and condition[2]=="<=" and unary== 1) or
                (condition[3]==name and condition[2]==">=" and unary == 1)
            ):
                self.repeatStatements(name,start,end+1,unary,statements)

            # for (int i=30; i>=0; i--)
            # for (int i=30; 0<=i; i--)
            elif ((condition[1]==name and condition[2]==">=" and unary== -1) or
                (condition[3]==name and condition[2]=="<=" and unary== -1)
            ):
                self.repeatStatements(name,start+1,end,unary,statements)
   
    def repeatStatements(self,name,start,end,unary,statements): 
        for i in range(start,end,unary):
            self.avatarLaLeyendaDeAang(statements)
            self.assignvar(name,str(int(self.getvar(name))+unary))

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
            if (statement != "operation" and statement != "") and (statement!="ifcondition"):
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
            if re.search(r"else\telse", statement):
                return re.split(r"\t", statement)[-1]
            elif re.search(r"\t", statement):
                newStatement.append( re.split(r"\t", statement)[-1] )
            else: 
                newStatement.append( statement )
        return newStatement

    # Evalua operaciones matemáticas
    def evalFunctionOperation(self, arrayVarStatement):
        op = arrayVarStatement[3:]
        strOp = "".join( op )
        if re.search(r"[a-zA-Z]\w*", strOp): 
            for i in range(len(op)): 
                if re.search(r"[a-zA-Z]\w*", op[i]): 
                    op[i] = self.getvar( op[i] )
            return eval( "".join( op ) )        
        else: 
            return eval( strOp )

    def avatarLaLeyendaDeAang(self,statements):
        for statement in statements:
            if statement[1]=="log":
                if(statement[-1] in self.variables):
                    self.printvarlog(statement[-1])
                else:
                    self.printlog(statement[-1])
            elif statement[1] == "error":
                if(statement[-1] in self.variables):
                    self.printvarerror(statement[-1])
                else:
                    self.printerror(statement[-1])
            elif statement[2] == "operation":
                self.assignvar(statement[1],self.assignOperation(statement))

    # Función If

    def ifdeclaration(self,condition,*args):
        condition = self.getValues(condition," ")
        statements = [
                        self.cleanDeclaration (
                            self.getValues(x,"#INDENT#") 
                        )
                        for x in args
                    ]
        elseIndex = self.cleanElseDeclaration(statements)

        if (self.cleanIfDeclaration(condition)):
            statements = statements[:elseIndex]
            self.avatarLaLeyendaDeAang(statements)
        elif (elseIndex is not 0):
            statements = statements[elseIndex+1:]
            self.avatarLaLeyendaDeAang(statements)

    # Evalua los párametros de una declaración if
    # retornando su valor de verdad
    def cleanIfDeclaration(self, arrayVarStatement ): 
        newStatement = self.cleanForStatement( arrayVarStatement )[1:]
        strOp = "".join( newStatement )
        if re.search(r"[a-zA-Z]\w*", strOp): 
            for i in range(len( newStatement )): 
                if re.search(r"[a-zA-Z]\w*", newStatement[i]): 
                    newStatement[i] = self.getvar( newStatement[i] )
            return eval( "".join(newStatement) )
        else: 
            return eval( strOp )

    #! Caso if else, pasando el arbol LARK completo
    #! Esta wea elimina una posicion del arreglo
    def cleanElseDeclaration(self, arrayVarStatement): 
        for i in range(len(arrayVarStatement)):
            if arrayVarStatement[i] == "else":
                return i
        return 0
            
    # Ciclo While

    def while_loop(self,condition,*args):
        if (str(type(condition))=="<class 'lark.tree.Tree'>"): 
            condition = self.getValues(condition," ")
            condition = [re.split(r"\t", x)[-1] for x in condition]
            if (len(condition)>1):
                condition = self.cleanIfDeclaration(condition)
            else:
                condition = bool(condition[0].title()
        elif (str(type(condition))=="<class 'lark.lexer.Token'>"):
            condition = self.getvar(condition).title()        