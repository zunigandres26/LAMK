# -*- coding: utf-8 -*-

"""
    @author Alexis
    @author Kenneth
    @date 2020/08/16
    @version 0.3    
"""

import re
from lark import Transformer, v_args, Tree


# La Clase Semantic contiene todos los alias de la gramática para simular la ejecución de un sencillo programa de Javascript.
@v_args(inline=True)
class Semantic(Transformer):

    # Constructor
    def __init__(self):
        self.variables = {} # Diccionario de Variables
        self.functions = {} # Diccionario de Funciones

    # Length
        """
            La función getlenght devuelve la longitud de cualquier variable definida para este proyecto, incluye:

                - String (Devolverá la cantidad de letras en la cadena)
                - booleano (undefined)
                - integer (undefined)
                - float (udefined)
                - null (No tiene atributo length)
        """
    def getlength(self,var):
        value = self.getvar(var)
        if (re.match(r"(\d+(\.\d+)?)|true|false",value)):
            print("Undefined")
        elif (re.match(r"(\"[^\"]*\")|('[^']*')",value)):
            print ("La longitud de la variable '%s' es: %d " % (var,len(self.cleanParam(value))))
        else:
            print("La variable '%s' no tiene atributo length" % var)

    # printLog
        """
            printLog Imprime el valor del parámetro text en un color verde.
            @params text: Texto a Imprimir
        """
    def printlog (self,text):
        print("\033[0;32m%s" % self.cleanParam(text))

    # printerror
        """
            printerror Imprime el valor del parámetro text en un color rojo.
            @params text: Texto a Imprimir
        """
    def printerror (self,text):
        print("\033[0;1;31m%s" % self.cleanParam(text))
    
    # printvarlog
        """
            printvarlog Imprime el valor de una variable en color verde.
            @params var: variable a la cual se recuperará su valor, si existe.
        """
    def printvarlog (self,var):
        self.printlog(self.cleanParam(self.getvar(var)))

    # printvarerror
        """
            printvarerror Imprime el valor de una variable en color rojo.
            @params var: variable a la cual se recuperará su valor, si existe.
        """
    def printvarerror (self,var):
        self.printerror (self.cleanParam(self.getvar(var)))

    # sum
        """
            La función sum Suma dos números enteros o flotantes.
            @param A: Primer Número
            @param B: Segundo Número
            @return Suma de A y B
        """
    def sum(self, A, B):
        if (isinstance(A,int) and isinstance(B,int)):
            return int(A)+int(B)
        else:
            return float(A)+float(B)
    # sub
        """
            La función sub Resta dos números enteros o flotantes.
            @param A: Primer Número
            @param B: Segundo Número
            @return Resta de A y B
        """
    def sub(self,A,B):
        if (isinstance(A,int) and isinstance(B,int)):
            return int(A)-int(B)
        else:
            return float(A)-float(B)

    # mul
        """
            La función mul Multiplica dos números enteros o flotantes.
            @param A: Primer Número
            @param B: Segundo Número
            @return Producto de A y B
        """
    def mul(self,A,B):
        if (isinstance(A,int) and isinstance(B,int)):
            return int(A)*int(B)
        else:
            return float(A)*float(B)

    # div
        """
            La función div Divide dos números enteros o flotantes.
            @param A: Primer Número
            @param B: Segundo Número
            @return División de A entre B
        """
    def div(self,A,B):
        if int(B) is not 0:
            if (isinstance(A,int) and isinstance(B,int)):
                return int(A)/int(B)
            else:
                return float(A)/float(B)
        else:
            self.printerror("Infinito chaval, como el universo")

    # assignvar
        """
            La función assignvar guarda en el diccionario 'variables' a la variable con su respectivo valor.
            @param name: Nombre de la variable.
            @param value: Valor de la variable.
        """
    def assignvar(self,name,value):
        
        if (str(type(value))=="<class 'lark.tree.Tree'>"):
            self.variables[str(name)] = value.data
        else:
            self.variables[str(name)] = value

    # cleanParam
        """
            cleanParam limpia una cadena de comillas simples o dobles.
            @param param: Cadena a limpiar.
        """
    def cleanParam(self,param):
        if re.match(r"^((\"[^\"]*\")|('[^']*'))$",param):
            return param[1:-1]
        return param

    # getvar
        """
            La función getvar recupera el valor de una variable dada.
            @param name: Nombre de la variable.
            @return string: valor de la variable.
        """
    def getvar(self,name):    
        return str(self.variables[str(name)])

    # forfunction
        """
            forfunction es el alias para la gramática de un ciclo for convencional en Javascript.
            Ejecuta las siguientes formas:
                
                -for (i = 0; i<10;i++){ statements }
                -for (j; j>a; i--){ statements }

            forfunction simula la ejecución de un ciclo for en Javascript mediante Python.

            @param name: Nombre de la variable declarada en el ciclo, e.g.: i,j.
            @param value: Valor de la variable declarada en el ciclo.
            @param condition: La condición que debe cumplirse para que el ciclo se repita.
            @param unary: Indica el Incremento o Decremento de la variable.
            @param args: Es una tupla que contiene las sentencias en forma de árbol Lark.
        """
    def forfunction(self, name, value,condition,unary, *args):
        
        self.assignvar(name,value) # Asigna el valor de la variable declarada en el ciclo

        condition = self.getValues(condition," ") # Obtiene el arreglo que contiene la condición
        
        unary = self.getUnary(self.getValues(unary," ")[-1].strip()) # Evalua si se incrementa o decrementa 
        
        # Los statements son la lista parseada de un árbol de Lark con las sentencias a repetir.
        statements = [
                        self.cleanDeclaration (
                            self.getValues(x,"#INDENT#") 
                        )
                        for x in args
                    ]

        # Posibles casos para el ciclo For
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
    
    # repeatStatements
        """ 
            repeatStatements repite las sentencias guardadas en una lista, de esa manera se puede simular el for.
            @param name: nombre de la variable.
            @param start: valor de inicio de la variable.
            @param end: valor al cual se terminará el ciclo.
            @param unary: Incremento o Decremento.
            @param statements: Lista con las sentencias a ejecutar.
        """
    def repeatStatements(self,name,start,end,unary,statements): 
        for i in range(start,end,unary):
            self.avatarLaLeyendaDeAang(statements)
            self.assignvar(name,str(int(self.getvar(name))+unary))

    # assignOperation
        """
            La función assignOperation verifica si el en la sentencia pasada como parametro existe una operación aritmética para ser resuelta.
            En caso de haberla, la evalua y devuelve el resultado.
            De lo contrario devuelve cero.
            @param statements: Sentencia a Evaluar.
        """
    def assignOperation(self,  statements): 
        return self.evalFunctionOperation( statements )  if "operation" in statements else 0

    # getUnary
        """
            getUnary convierte el operador de decremento (--) o incremento(++) en su equivalente en Python (1,-1).
            @param unary: Incremento o Decremento.
            @return Integer: 1 o -1
        """
    def getUnary(self,unary):
        return 1 if unary=="++" else -1

    # getEnd
        """
            getEnd se encarga de obtener el valor final desde la lista con las condiciones.
            @param condition: arreglo con las condiciones.
            @param name: Nombre de la variable.
        """
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

    # getValues
        """
            La función getValues parsea un árbol de tokens de lark a una lista sobre la cual se puede iterar utilizando la función pretty la cual esta integrada sobre el objeto Tree de Lark.
            @param tree: árbol del tipo Lark.
            @param indent: Se refiere al símbolo que se utilizará para identar la representación del árbol en texto.
            @return tree: Árbol parseado a Lista.
        """
    def getValues (self,tree,indent):
        tree = tree.pretty(indent_str=indent).split(indent)
        tree = [x.strip() for x in tree]
        return tree

    # cleanDeclaration
        """
            cleanDeclaration Filtra las sentencias extraidas de un árbol de Lark.
            Estas sentencias pueden ser del tipo operación aritmética o general.
            @param arrayStatement: Sentencia a Limpiar.
        """
    def cleanDeclaration(self, arrayVarStatement ):
        if 'operation' in arrayVarStatement: 
            return self.cleanVarStatementDeclaration( arrayVarStatement )
        else: 
            return self.cleanForStatement( arrayVarStatement )


    # cleanVarStatementDeclaration
        """
            Esta función limpia las sentencias del tipo operación Aritmética.
            @param arrayVarStatement: Sentencia a Limpiar.
            @return list: Una lista con la operación limpia para procesar.
        """
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

    # cleanForStatement
        """
            cleanForStatement limpia sentencias con tabuldados y caracteres no deseados las cuales son extraidas del árbol Lark.
            @param arrayVarStatement: Sentencia con los valores a limpiar.
            @return newStatement: Lita con los valores limpios para procesar.
        """
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

    
    # evalFunctionOperation
        """
            evalFunctionOperation recibe una sentencia del tipo operación la cual es convertida a texto y luego evaluada con la ayuda de la función eval de python.
            @param arrayVarStatement: Arreglo con la sentencia del tipo operación.
            @return value: Valor final luego de realizar la operación.
        """
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

    # avatarLaLeyendaDeAang
        """
            avatarLaLeyendaDeAang controla las posibles apariciones de sentencias dentro de funciones, for's, if's y while's.
            Estas sentencias pueden ser impresiones de datos y asignaciones de variables.
            @param statements: Lista con las sentencias a evaluar.
        """
    def avatarLaLeyendaDeAang(self,statements):
        for statement in statements:
            if statement[1]=="log":
                if(
                    statement[-1] in self.variables
                ):
                    self.printvarlog(statement[-1])
                else:
                    self.printlog(statement[-1])
            elif statement[1] == "error":
                if(
                    statement[-1] in self.variables
                ):
                    self.printvarerror(statement[-1])
                else:
                    self.printerror(statement[-1])
            elif statement[2] == "operation":
                
                self.assignvar(statement[1],str(self.assignOperation(statement)))

    # ifdeclaration
        """
            ifdeclaration simula una función if. La cual puede estar escrita de las siguientes formas.

                - if (condicion) { statements }
                - if (condicion) { statements } else { statements }
            
            La función ifdeclaration acepta una cantidad variable de sentencias.

            @param condition: Condición de Veracidad.
            @param args: Tupla que contiene las sentencias del árbol Lark.
            @param function: Esta bandera indica si la función if se está ejecutando desde una función o no.
            @param ready: Indica si los parametros condition y args han sido parseados de un árbol Lark a una lista.
        """
    def ifdeclaration(self,condition,*args,function=False,ready=False):
        
        if (function and ready):
            statements = args[0]
        elif function:
            statements = []
            [statements.append(x) for x in args]
        else:
            condition = self.getValues(condition," ")
            statements = [
                            self.cleanDeclaration (
                                self.getValues(x,"#INDENT#") 
                            )
                            for x in args
                        ]
        
        elseIndex = self.cleanElseDeclaration(statements) # Encontrar la posición del Else, si existe.

        if (self.cleanIfDeclaration(condition)):
            if (elseIndex is not 0):
                statements = statements[:elseIndex]
            self.avatarLaLeyendaDeAang(statements)
        elif (elseIndex is not 0):
            statements = statements[elseIndex+1:]
            self.avatarLaLeyendaDeAang(statements)

    # cleanIfDeclaration
        """
            cleanIfDeclaration evalua la condición (verdadero o falso).
            @param arrayVarStatement: Arreglo con la sentencia de condición.
            @return boolean: True o False.
        """
    def cleanIfDeclaration(self, arrayVarStatement): 
        newStatement = self.cleanForStatement( arrayVarStatement )[1:]
        strOp = "".join( newStatement )
        if re.search(r"[a-zA-Z]\w*", strOp): 
            for i in range(len( newStatement )): 
                if re.search(r"[a-zA-Z]\w*", newStatement[i]): 
                    newStatement[i] = self.getvar( newStatement[i])
            return eval( "".join(newStatement) )
        else: 
            return eval( strOp )

    # cleanElseDeclaration
        """
            cleanElseDeclaration reemplaza la sentencia else por una cadena simple "else", la cual
            servirá como pivote para diferenciar la sentencia verdadera y falsa.
            @param arrayVarStatement: Lista con las sentencias Else If.
            @return array: Lista con las sentencias Else If, reemplazando la sentencia else por una cadena.
        """
    def cleanElseDeclaration(self, arrayVarStatement): 
        for i in range(len(arrayVarStatement)):
            if arrayVarStatement[i] == "else":
                return i
        return 0
            
    # while_loop
        """
            whilte_loop simula un ciclo While. La forma es:

                - while (condition) { statements }

            @param condition: Condición de veracidad.
            @param args: Tupla que contiene las sentencias del árbol Lark.
        """
    def while_loop(self,condition,*args):

        # Obtener la condición
        if (str(type(condition))=="<class 'lark.tree.Tree'>"): 
            condition = self.getValues(condition," ")
            condition = [re.split(r"\t", x)[-1] for x in condition]
            condition = self.getTextCondition(condition)
        elif (str(type(condition))=="<class 'lark.lexer.Token'>"):
            condition = str(self.getvar(condition))

        # Parsear el árbol
        statements = [
                        self.cleanDeclaration (
                            self.getValues(x,"#INDENT#") 
                        )
                        for x in args
                    ]

        while (self.evalTextCondition(condition)):
            self.avatarLaLeyendaDeAang(statements)  

    # getTextCondition
            """
                getTextCondition obtiene la condición de un while en su equivalente en texto.
                @param condition: Lista con la condición del While.
                @retun string: Condición en forma de Texto.
            """
    def getTextCondition(self,condition):
        if len(condition)>1:
            return " ".join(condition[1:])
        else:
            return condition[0]

    # evalTextCondition
        """
            evalTextCondition evalua una condición en texto y devuelve su valor de verdad.
            @param condition: Condición en forma de cadena.
            @return boolean: True o False.
        """
    def evalTextCondition(self,condition):
        condition = condition.split(" ")
        for i in range(len(condition)):
            if (re.match(r"true|false",condition[i])):
                condition[i]= condition[i].title()
            elif (re.match(r"[a-zA-Z]\w*",condition[i])):
                condition[i] = str(self.getvar(condition[i]))
                if (re.match(r"true|false",condition[i])):
                    condition[i]=condition[i].title()
                    
        condition = " ".join(condition)
        return bool(eval(condition))

    # declarefunction
        """
            declarefunction simula la declaración de una función en Javascript. Su forma es:

                - function name ( parameters ) { statements }

            La función se almacena en el diccionario de funciones y no es ejecutada hasta que es llamada.

            @param name: Nombre de la función.
            @param parameters: Parametros de la función (máximo de 2).
            @param args: Tupla que contiene las sentencias del árbol Lark.
        """
    def declarefunction(self,name,parameters,*args):
        
        # Obteniendo los Parametros
        if (str(type(parameters))=="<class 'lark.tree.Tree'>"): 
            parameters = self.getValues(parameters,"#INDENT#")[1:]
        elif (str(type(parameters))=="<class 'lark.lexer.Token'>"):
            parameters = [str(parameters)]

        # Parseando el árbol de Lark
        statements = [
                        self.getValues(x,"#INDENT#") 
                        for x in args
                    ]
        
        cleanStatements = self.cleanTree(statements)
        
        self.functions[str(name)] = [parameters,self.classify(cleanStatements)]
    
    # countOcurrences
        """
            countOcurrences cuenta cuantas veces se encuentra una palabra en una lista.
            @param word: Palabra a buscar.
            @param array: Lista en la cual se buscará la palabra.
        """
    def countOccurrences(self,word,array):
        c = 0
        for i in array:
            if i == word:
                c+=1
        return c

    # cleanTree
        """
            cleanTree Limpia una lista de valores basura como valores en blanco y caracteres no deseados como tabulados.
            @param statements: Lista con las sentencias de un árbol Lark.
            @return cleanStatements: Lista con las sentencias limpias.
        """
    def cleanTree(self,statements):
        cleanStatements = []
        for x in statements:
            newStatement = []
            for y in x:
                if re.search(r"\t",y):
                    newStatement.append( re.split(r"\t", y)[-1] )
                elif ((y is not "") and (y != "iffunc") and (y is not "r")):
                    newStatement.append(y)
            cleanStatements.append(newStatement)

        return cleanStatements

    # classify
        """
            classify clasifica las sentencias de una lista, las cuales pueden ser:
                - condiciones If
                - Declaraciones If de una línea
                - Declaraciones If-Else
                - Asignaciones de Variables
                - Impresión de cadenas
                - Impresión de Variables

            @param cleanStatements: Lista con las sentencias ya limpiadas por cleanTree.
            @return result: Lista de Tuplas que contienen la clasificación de las sentecias.
        """
    def classify(self,cleanStatements):
        result=[]

        for x in cleanStatements:
            if ('else' in x):
                result.append(("ElseIf",x))
            elif (
                'ifcondition' in x and 
                (
                    self.countOccurrences("varstatementdeclaration",x)==1 or 
                    self.countOccurrences("statements",x)==1 or 
                    self.countOccurrences("return",x) == 1
                )
            ):
                result.append(("OneLineIf",x))
            elif (self.countOccurrences("varstatementdeclaration",x)==1):         
                result.append(("varDeclaration",x))
            elif (self.countOccurrences("log",x)==1) :
                result.append(("printLog",x))   
            elif (self.countOccurrences("error",x)==1):
                result.append(("printError",x)) 
            elif (self.countOccurrences("return",x) == 1):
                result.append(("return",x)) 

        return result

    # functioncall
        """
            functioncall se refiere al llamado de una función la cual ha sido declarada.
            @param name: Nombre de la función.
            @param parameters: Bandera para los parametros, por Defecto None.
        """
    def functioncall (self,name,parameters=None):
        
        # Obtener los parámetros, si existen.
        if (str(type(parameters))=="<class 'lark.tree.Tree'>"): 
            parameters = self.getValues(parameters,"#INDENT#")[1:]
        elif (str(type(parameters))=="<class 'lark.lexer.Token'>"):
            parameters = [str(parameters)]

        if (str(name) in self.functions):
            
            if (len(self.functions[str(name)][0]) == len(parameters)):
                
                for i in range(len(parameters)):
                    
                    if re.match(r"true|false",parameters[i]):
                        pass # Verificamos que es un tipo de dato conocido, pero no es necesario hacer algo.
                    elif re.match(r"[a-zA-Z]\w*",parameters[i]):
                        if parameters[i] in self.variables:
                            parameters[i] = self.getvar(parameters[i])
                        else: 
                            quit("La variables '%s' No existe" % parameters[i]) # Captura de Error. La variable no Existe.

                    elif ( (re.match(r"('[^']*')|(\"[^\"]*\")",parameters[i])) or (re.match(r"\d+(\.\d+)?",parameters[i])) ):
                        pass # Verificamos que es un tipo conocido, pero no es necesario hacer algo.
                    else:
                        quit("No se reconoció el tipo de dato: %s" % parameters[i]) # Captura de Error. Tipo de Dato Desconocido.
                
                self.executeFunction(name,self.functions[str(name)][1],parameters) # Ejecución de la Función.

            else:
                quit ("Parametros Incorrectos: function %s " % str(name))# Captura de Error. La cantidad de parametros enviados es incorrecta.
        else:
            print ("La función '%s' no existe." % (str(name))) # Captura de Error. La función no Existe.

    # executeFunction
            """
                executeFunction ejecuta la función llamada luego de ser verificada.
                @param name: Nombre de la función.
                @param statements: Se refiere a las sentencias contenidas en la función.
                @param parameters: Parametros de la función.
            """
    def executeFunction (self, name,statements,parameters):

        # Asignar los valores a los parametros
        for i in range(len(self.functions[str(name)][0])):
            self.assignvar(self.functions[str(name)][0][i],str(parameters[i]))


        # Avatar, La leyenda de Aang pero más op
        # Dentro de este ciclo for se toman las decisiones de acuerdo a la clasificación dada por classify.
        for i in statements:

            # Console Log, Console varLog
            if i[0] == "printLog":
                if  re.match(r"[a-zA-Z]\w*",i[1][2]):
                    self.printvarlog(i[1][2])
                else:
                    self.printlog(i[1][2])

            # Console Error, Console varError
            elif i[0] == "printError":
                if  re.match(r"[a-zA-Z]\w*",i[1][2]):
                    self.printvarerror(i[1][2])
                else:
                    self.printerror(i[1][2])

            # varDeclaration , evalFunctionOperation
            elif i[0] == "varDeclaration":
                if "operation" in i[1]:
                    operation = i[1][3:]
                    strOperation = [i[1][0],i[1][1],i[1][2]]
                    for op in operation:
                        if op != "operation":
                            strOperation.append(op)
                    self.assignvar(i[1][1],self.evalFunctionOperation(strOperation))
                else:
                    self.assignvar(i[1][1],i[1][2])

            # OneLineIf
            elif i[0] == "OneLineIf":
                condition = i[1][:4]
                statement = i[1][4:]
                
                if "operation" in statement:
                    operation = statement[3:]
                    cleanStatement = statement[:3]
                    for op in operation:
                        if op != "operation":
                            cleanStatement.append(op)
                    self.ifdeclaration(condition,cleanStatement,function=True)
                else:
                    self.ifdeclaration(condition,statement,function=True)

            # ElseIf
            elif i[0] == "ElseIf":
                condition = i[1][:4]
                statements = i[1][4:]    

                pizza = self.slicedPizza(statements)
                self.ifdeclaration(condition,pizza,function=True,ready=True)
                
    
    # slicedPizza
        """
            slicedPizza recibe toda la sentencia como un arreglo unidimensional el cual es "cortado"
            y convertido en un arreglo bidimensional, separando las Sentencias de manera que puedan
            ser procesadas de manera correcta.
            @param statements: Arreglo unidemensional con las sentencias contenidas en la función.
            @return tokenizedStatements: Lista bidimensional con las sentencias ordenadas de manera adecuada.
        """
    def slicedPizza(self,statements):
        tokenizedStatements = []
        i = 0
        while (i<len(statements)):

            if (statements[i]=="statements"):
                tokenizedStatements.append([statements[i],statements[i+1],statements[i+2]])
                i+=3
                
            elif (statements[i]=="varstatementdeclaration"):
                statement = [statements[i]]
                i+=1
                while(
                    statements[i]!= "varstatementdeclaration" and 
                    statements[i]!= "statements" and
                    statements[i]!= "else" 
                ):
                    statement.append(statements[i])
                    i+=1
                    if i==len(statements):
                        break
                tokenizedStatements.append(statement)
            
            elif (statements[i]=="else"):
                tokenizedStatements.append(statements[i])
                i+=1

        for i in range(len(tokenizedStatements)):
            if "operation" in tokenizedStatements[i]:
                cleanStatement = []
                operation = tokenizedStatements[i][3:]
                cleanStatement = tokenizedStatements[i][:3]
                for op in operation:
                    if op != "operation":
                        cleanStatement.append(op)
                tokenizedStatements[i] = cleanStatement

        return tokenizedStatements