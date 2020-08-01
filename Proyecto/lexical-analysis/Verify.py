# -*- coding: utf-8 -*-

class Verify: 

    def __init__(self): 
        pass

    # Condiciones
    def isDigit(self, char): 
        return True  if char >= 48 and char <= 57 else False

    # Punto
    def isDot(self, char): 
        return True if char == 46 else False

    # Salto de linea y tabulados
    def isLineBreak(self, char): 
        return True if char >= 9 and char <= 10 else False

    # Comilla doble
    def isQuote(self, char): 
        return True if char == 34 else False

    # Comilla simple
    def isQuoteSimple(self, char): 
        return True if char == 39 else False

    # a-z A-Z
    def isAlphabet(self, char): 
        return True if (
            (char >= 65 and char <= 90) or # Mayúsculas
            (char >= 97 and char <= 122)   # Minúsculas
        ) else False 

    # Espacio en blanco
    def whitespace(self, char): 
        return True if char == 32 else False

    # Identificador de usuario
    def isID(self, char): 
        return True if ( self.isAlphabet( char )  or self.isDigit( char ) or char == 95) else False

    #all spaces white
    def isAllSpaceswhite(self, char): 
        return True if (self.isLineBreak( char  ) or self.whitespace( char )) else False


    #---------------------------------------------------------------
    #                     Operadores de comparación
    #---------------------------------------------------------------

    # Operador menor que 
    def isLessThan(self, char): 
        return True if char == 60 else False 

    # Operador de asignación 
    def isAssignment(self, char): 
        return True if char == 61 else False 

    # Operador mayor que 
    def isGreaterThan(self, char): 
        return True if char == 62 else False 

    #Not equal 
    def isNotEqual(self, char): 
        return True if char == 33 else False 
    

    #---------------------------------------------------------------
    #                     Operadores aritméticos
    #---------------------------------------------------------------

    # Operador de suma
    def isSummop(self, char): 
        return True if char == 43 else False 

    # Operador de resta
    def isSubop(self, char): 
        return True if char == 45 else False 

    # Operador de multiplicación
    def isMultop(self, char): 
        return True if char == 42 else False 

    # Operador de división
    def isDivideop(self, char): 
        return True if char == 47 else False 