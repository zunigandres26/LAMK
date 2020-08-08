from Statement import *
from Verify import *
import re

class SyntaxAnalyzer:

    def __init__(self, reader):
        self.text = reader.text
        self.verify = Verify()
        self.statements = []
        self.language = 0

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
        return self.innerRun( firstLine, lastLine, lines)
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
                not self.verify.isOpenComment( statement.atFirst(), self.language )
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
                quit("Lenguaje %s\nError de Sintaxis en linea \n%s\nflujo mal cerrado"
                    % (self.getLanguage( self.language ), statement.atFirst())
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
        
        if(
            not statement.InAnalysis and
            (
            self.language == 0 or
            self.language > 3
            ) and
            not self.verify.isBlank( line )
        ):
            self.language = self.verify.isWhatLanguage( line )
            """
            -----------------------------------------------------
            Esta condicion se encarga de verificar a que lenguaje
            pertenece la linea actual; si la linea actual es un 
            Statement de varios lenguajes, Entonces:
            self.language sera mayor a 4
            ------------------------------------------------------
            """
        if (
            not statement.InAnalysis and
            self.verify.isOneLineOpenFlow( line, self.language ) and
            not self.verify.isOpenKeyword( line, self.language ) 
        ):
            statement.InAnalysis = True
            statement.type = "flow statement"
            statement.add( line )
            statement.analyzed = False
            statement.forClose += 1
            """
            -----------------------------------------------------
            El incio de todas las estructura de control de flujo
            que necesitan 1 lineas.
            Eg:. if (condicion) {
            ------------------------------------------------------
            """
        elif(
            not statement.InAnalysis and
            self.verify.isTwoLinesOpenFlow( line, self.language )
        ):
            statement.InAnalysis = True
            statement.type = "flow statement"
            statement.add( line )
            statement.analyzed = False
            """
            -----------------------------------------------------
            El inicio de todas las estructuras de control de flujo
            que necesitan 2 lineas
            Eg:. if (condicion)
                 { 
            ------------------------------------------------------
            """
        elif (
            not statement.InAnalysis and
            not self.verify.isOpenKeyword( line, self.language ) and
            self.verify.isOneLineStatement( line, self.language )
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
            self.verify.isOpenKeyword( line, self.language )
        ):
            pass
            """
            -----------------------------------------------------
            Las openKeywords son caracteres o palabras claves que
            abren una estructura de control de flujo.
            Por ejemplo { , do , begin
            ------------------------------------------------------
            """
        
        elif(
            not statement.InAnalysis and
            not self.verify.isBlank( line )
        ):
            quit("Lenguaje de Programacion %s \nError sintactico: se ha encontrado un error en la linea %d\n %s"
            % (self.getLanguage(self.language),(pos+1), line)
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
                self.verify.isAnyLinesOpenFlow( statement.atFirst(), self.language )and
                not self.verify.isOneLineOpenFlow( line, self.language ) and
                not self.verify.isCloseFlow( line, self.language )
            ):
                statement.add( line )

            elif(
                self.verify.isAnyLinesOpenFlow( statement.atFirst(), self.language )and
                self.verify.isOneLineOpenFlow( line, self.language ) and
                not self.verify.isOpenComment( statement.atFirst(), self.language )
            ):
                statement.add( line )
                statement.forClose += 1
            elif(
                self.verify.isAnyLinesOpenFlow( statement.atFirst(), self.language )and
                self.verify.isCloseFlow( line, self.language ) and
                not self.verify.isOpenComment( statement.atFirst(), self.language )
                
            ):
                statement.add( line )
                statement.forClose -= 1
                if statement.forClose == 0:
                    statement.analyzed = True
                    statement.InAnalysis = False
            elif(
                self.verify.isOpenComment( statement.atFirst(), self.language ) and
                not self.verify.isCloseComment( line, self.language )
            ):
                statement.add( line )
            elif(
                self.verify.isOpenComment( statement.atFirst(), self.language ) and
                self.verify.isCloseComment( line, self.language )
                
            ):
                statement.add( line )
                statement.forClose -= 1
                if statement.forClose == 0:
                    statement.analyzed = True
                    statement.InAnalysis = False
              
        else: 
            statement = Statement()
        pos += 1

        return (pos, statement)
        
    
    def getLanguage(self, i):
        if i == 1:
            return "Javascript"
        if i == 2:
            return "Bash"
        if i == 3:
            return "Ruby"



