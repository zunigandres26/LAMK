from Statement import *
from Verify import *
import re

class SyntaxAnalyzer:

    def __init__(self, reader):
        self.text = reader.text
        self.verify = Verify()
        self.statements = []

    def run(self):
        #self.verify.printRe()
        """
        -----------------------------------------------------
        La linea 13 imprime una RE, y esta se escoge en la
        clase Verify
        ------------------------------------------------------
        """ 
        lines = re.split(r"\n", self.text)

        firstLine = 0
        lastLine = len( lines )
        return self.innerRun( firstLine, lastLine, lines )
        """
        -----------------------------------------------------
        Este metodo establece una ejecucion inicial del metodo
        innerRun
        ------------------------------------------------------
        """


    def innerRun(self, i, j, lines):
        statement = None
        while( i < j ):
            i, statement = self.statementCreator(lines, i, statement) 

            if statement.analyzed: 
                self.statements += [ statement ]
            if(
                statement.analyzed and
                statement.type == "flow statement" and 
                not self.verify.isOpenComment( statement.atFirst() )
            ):
                firstLine = (i-len( statement.lines )) + 1
                lastLine = (i-1)
                self.innerRun(firstLine, lastLine, lines)
                """
                -----------------------------------------------------
                Si el analisis de la declaracion es correcto y esta
                es un control de flujo pero No un comentario de 
                multiples lineas, entonces se procedera a analizar
                las declaraciones que esta tenga adentro
                ------------------------------------------------------
                """
            if( 
                i == (len( lines )) and
                not statement.forClose == 0
            
            ):
                quit("Error de Sintaxis en linea \n%s\nflujo mal cerrado"
                    % statement.atFirst()
                )
                """
                -----------------------------------------------------
                Si se detecta que existen estructuras de control de
                flujo sin cerrarse:
                habra error de sintaxis
                ------------------------------------------------------
                """
                                
        return self
        """
        -----------------------------------------------------
        Este metodo se ejecuta de forma recursiva dependiendo
        de la cantidad de declaraciones de control de flujo
        que existan en el archivo a analizar.
        ------------------------------------------------------
        """

    def statementCreator(self, lines, i, statement):
        if not statement or statement.analyzed:
            statement = Statement()

        line, pos = lines[i], i
    
        if (
            not statement.InAnalysis and
            self.verify.isOpenFlow( line )
        ):
            statement.InAnalysis = True
            statement.type = "flow statement"
            statement.add( line )
            statement.analyzed = False
            statement.forClose += 1
            """
            -----------------------------------------------------
            El incio de todas las estructura de control de flujo
            y funciones:
            for, while, if, function
            ------------------------------------------------------
            """
        elif (
            not statement.InAnalysis and
            self.verify.isOneLineStatement( line )
        ):
            statement.InAnalysis = False
            statement.type = "one line statement"
            statement.add( line )
            statement.analyzed = True
            """
            -----------------------------------------------------
            Todas las declaraciones que solo abarcan una linea:
            if de una linea, asignacion de variables, llamado de
            funciones, return
            ------------------------------------------------------
            """
        elif(
            not statement.InAnalysis and
            not self.verify.isBlank( line )
        ):
            quit("Error sintactico: se ha encontrado un error en la linea %d\n %s"
            % ((pos+1), line)
            )
            """
            -----------------------------------------------------
            En caso de que no se reconozca si la sintaxis de la 
            linea pertenece al inicio de control de flujo o a una
            declaracion de una sola linea:
            La sintasis de la linea estara incorrecta. 
            ------------------------------------------------------
            """
        elif(
            statement.InAnalysis
        ):  
            """
            -----------------------------------------------------
            Inicio de casos para formar la declaracion de una
            estructuras de control de flujos
            ------------------------------------------------------
            """
            if(
                self.verify.isOpenFlow( statement.atFirst() ) and
                not self.verify.isOpenFlow( line ) and
                not self.verify.isCloseFlow( line )
            ):
                statement.add( line )

            elif(
                self.verify.isOpenFlow( statement.atFirst() ) and
                self.verify.isOpenFlow( line )
            ):
                statement.add( line )
                statement.forClose += 1
            elif(
                self.verify.isOpenFlow( statement.atFirst() ) and
                self.verify.isCloseFlow( line )
            ):
                statement.add( line )
                statement.forClose -= 1
                if statement.forClose == 0:
                    statement.analyzed = True
                    statement.InAnalysis = False
            
            """
            -----------------------------------------------------
            final de casos para formar la declaracion de una 
            estructura de control de flujos
            ------------------------------------------------------
            """
        else: 
            statement = Statement()
        pos += 1

        return (pos, statement)
        """
        -----------------------------------------------------
        Este metodo se encarga de verificar si el analisis de 
        la estructura de una declaracion es correcta.
        ------------------------------------------------------
        """
        


