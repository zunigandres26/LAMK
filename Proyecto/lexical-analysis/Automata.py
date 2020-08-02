# -*- coding: utf-8 -*-

from Token import Token 
from Verify import Verify

class Automata: 

    def __init__(self, reader): 
        self.reader = reader
        self.verify = Verify()

    def run(self): 
        text = self.reader.text + " "
        tokens = []

        i = 0 
        token = None 
        while(i < len(text)): 

            i, token = self.tokenCreator(text, i, token) 

            if token.formed: 
                tokens += [ token ]
            #print( [token.info()[0] for token in tokens], token.formed )
        self.tokens = tokens
        return self

    def tokenCreator(self, text, i, token): 
        if not token or token.formed: 
            token = Token()

        char, pos = ord(text[i]), i

        #---------------------------------------------------------------
        #                    Condiciones | Aristas
        #---------------------------------------------------------------

        #Número
        if(
            not token.inFormation and 
            self.verify.isDigit(char)
        ): 
            token.add(char)
            token.formed = False
            token.inFormation = True 
            token.type = "Number"
        
        #Comilla doble
        elif(
            not token.inFormation and 
            self.verify.isQuote(char)
        ): 
            token.add(char)
            token.formed = False
            token.inFormation = True
            token.type = "String"

        #Comilla simple
        elif(
            not token.inFormation and 
            self.verify.isQuoteSimple(char)
        ): 
            token.add(char)
            token.formed = False
            token.inFormation = True
            token.type = "String"

        #identificador de usuario
        elif( 
            not token.inFormation and 
            self.verify.isAlphabet( char )
        ): 
            token.add( char )
            token.formed = False
            token.inFormation = True
            token.type = "User identifier"

        # Operador de Asignación 
        elif(
            not token.inFormation and 
            self.verify.isAssignment( char )
        ):
            token.add( char )
            token.formed = False 
            token.inFormation = True 
            token.type = "Assignment operator"

        # Operador menor que 
        elif(
            not token.inFormation and 
            self.verify.isLessThan( char )
        ): 
            token.add( char )
            token.formed = False
            token.inFormation = True 
            token.type = "Less than operator"

        # Operador mayor que 
        elif(
            not token.inFormation and 
            self.verify.isGreaterThan( char )
        ): 
            token.add( char )
            token.formed = False
            token.inFormation = True 
            token.type = "Greater than operator"

        #-------NUEVO------
        # Operador de multiplicación
        elif(
            not token.inFormation and
            self.verify.isMultop ( char )
        ):
            token.add( char )
            token.formed = True
            token.inFormation = False
            token.type = "Multiply operation"

        #-------NUEVO------
        # Operador de resta
        elif(
            not token.inFormation and
            self.verify.isSubop ( char )
        ):
            token.add( char )
            token.formed = True
            token.inFormation = False
            token.type = "Subtraction operation"


        #-------NUEVO------
        # Operador de suma
        elif(
            not token.inFormation and
            self.verify.isSubop ( char )
        ):
            token.add( char )
            token.formed = True
            token.inFormation = False
            token.type = "Subtraction operation"

             
        # Apertura de parentesis
        elif(
            not token.inFormation and
            self.verify.isOpenParenthesis ( char )
        ):
            token.add( char )
            token.formed = True
            token.inFormation = False
            token.type = "Open parenthesis"

        
        # Cierre de parentesis
        elif(
            not token.inFormation and
            self.verify.isCloseParenthesis ( char )
        ):
            token.add( char )
            token.formed = True
            token.inFormation = False
            token.type = "Close parenthesis"

        # Apertura de Llave
        elif(
            not token.inFormation and
            self.verify.isOpenCurlyBrace ( char )
        ):
            token.add( char )
            token.formed = True
            token.inFormation = False
            token.type = "Open Curly Brace"
        
        # Cierre de Llave
        elif(
            not token.inFormation and
            self.verify.isCloseCurlyBrace ( char )
        ):
            token.add( char )
            token.formed = True
            token.inFormation = False
            token.type = "Close Curly Brace"
        
        # Coma
        elif(
            not token.inFormation and
            self.verify.isComma ( char )
        ):
            token.add( char )
            token.formed = True
            token.inFormation = False
            token.type = "Comma"
        
        # Punto y coma
        elif(
            not token.inFormation and
            self.verify.isSemicolon ( char )
        ):
            token.add( char )
            token.formed = True
            token.inFormation = False
            token.type = "End of statement"

        elif( 
                token.inFormation 
            ):
                # Cadena con doble comilla
                if (
                    self.verify.isQuote( token.atFirst() ) and 
                    not self.verify.isQuote( char )
                ): 
                    token.add( char )

                # Cadena con comilla simple
                elif (
                    self.verify.isQuoteSimple( token.atFirst() ) and 
                    not self.verify.isQuoteSimple( char )
                ): 
                    token.add( char )

                # Identificador de usuario
                elif (
                    self.verify.isAlphabet( token.atFirst() ) and 
                    self.verify.isID( char )
                ): 
                    token.add( char )

                elif(
                    self.verify.isAlphabet( token.atFirst() ) and 
                    not self.verify.isID( char )
                ):
                    token.formed = True
                    token = self.verify.isKeyword(token) #-- Aquí puse la verificación -- NUEVO
                    pos-=1 #NUEVO

                # Flotante 
                elif (
                    self.verify.isDigit( token.atFirst() ) and 
                    self.verify.isDot( char )
                ): 
                    token.add( char )
                    token.type = "Float"

                # Digito
                elif (
                    self.verify.isDigit( token.atFirst() )  and 
                    #not (self.verify.isLineBreak( char  ) or self.verify.whitespace( char ))
                    self.verify.isDigit( char ) 
                ): 
                    token.add( char )

                # Igualdad
                elif(
                    self.verify.isAssignment( token.atFirst() ) and 
                    self.verify.isAssignment( char )
                ): 
                    token.add( char )
                    token.type = "Equal operator"
                    token.formed = True

                # Menor o igual
                elif(
                    self.verify.isLessThan( token.atFirst() ) and 
                    self.verify.isAssignment( char )   
                ): 
                    token.add( char )
                    token.type = "Less than or equal operator"

                # Mayor o igual
                elif(
                    self.verify.isGreaterThan( token.atFirst() ) and
                    self.verify.isAssignment( char ) 
 
                ): 
                    token.add( char )
                    token.type = "Greater than or equal operator"

                else:
                    # Por aquí borre un if que no servia de nada :v

                    if self.verify.isLineBreak(char): #Elimina tabulados y saltos de linea
                        token.inFormation = False 

                    #-------NUEVO------
                    elif (
                        self.verify.isQuote( token.atFirst() ) and 
                        self.verify.isQuote( char )
                    ): 
                        token.add( char )
                        token.inFormation = True
                    
                    else:
                        #token.add( char )
                        pos -= 1 #-------NUEVO------
                    """else: 
                        token.add( char )
                    """

                    token.formed = True 
        else: 
            token = Token()
        pos += 1

        #print( token.info()[0] )

        return (pos, token)

