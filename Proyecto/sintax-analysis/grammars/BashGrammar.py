
import re

"""
-----------------------------------------------------
Clase Gramatica del Lenguaje Bash
------------------------------------------------------
""" 
class BashGrammar:

    def __init__(self):
        
        #Variables
        self.var = "[A-Za-z][A-Za-z0-9_]*"

        #Call Variables
        self.callVar = ("\$%s".strip()
            % self.var
        ).strip()

        #Data Types
        self.string = "(\"[^\"]*\"|'[^']*')"
        self.number = "[0-9]+"
        self.boolean = "(true|false)"

        #Variables and Data Types
        self.allDataTypes = ("(%s|%s|%s|%s|%s)".strip() 
            % (self.var, self.string, self.number, self.boolean, self.callVar)
                            )

        #Operators para comparar cadenas
        self.stringOperators = "(=|==|>|>=|<|<=)"

        #Operadores para comparar Enteros
        self.intOperators = "(-gt|-lt|-ge|-le|-eq|-ne)"

        #Operadores Booleanos
        self.booleanOperators = "(-a|-o)"

        #All Operators
        self.allOperators = ("(%s|%s|%s)".strip()
            % (self.intOperators, self.stringOperators, self.booleanOperators)
        ).strip()


        #Counters
        self.counters = ("%s\+\+|%s\-\-".strip() % (self.var, self.var))

        #Conditional
        self.opCondicional = ("\s*%s\s*%s\s*%s\s*".strip()
                % (self.allDataTypes, self.allOperators, self.allDataTypes)
                        ).strip()

        #var assignment
        self.assignment = ("\s*%s=(%s|%s|%s|%s|%s)\s*".strip()
                    % (self.var, self.number, self.string, self.var, self.boolean, self.callVar)
                        )

        #Integer Only Assignment
        self.intAssignment = ("\s*%s\s*=\s*%s\s*".strip()
                            % (self.var, self.number)
                        )
        
        #Params
        self.params = ("\s*%s\s*\,?\s*(%s)?\s*" % (self.var, self.var))

        #Close Bracket
        self.closeBracket = "\s*}\s*"

        #Close if
        self.closeIF = "\s*fi\s*"

        #Close if
        self.closeFor = "\s*done\s*"
        
        #Open multiple comments
        self.openMultipleComment = ("\s*\/\*\s*[^\/\*]*\s*")

        #Blank Space
        self.blank = "(\s|\t|\n)*"

        #Param function
        self.paramFunction = ("\s*%s.?%s?\(\s*%s\s*\)\s*".strip()
                    % (self.var, self.var, self.var)
                            ).strip()

        #Call Function Params
        self.callParams = ("\s*(%s|%s)?\s*\,?\s*(%s|%s)?\s*".strip()
                    % (self.allDataTypes, self.paramFunction, self.allDataTypes, self.paramFunction)
                        ).strip()

        #then reserved keyword
        self.openIfKeyword = "\s*then\s*"

        #do reserved keyword
        self.openForKeyword = "\s*do\s*"

        #All the open flow reserved keywords
        self.allOpenKeyword = ("(%s|%s)".strip()
            % (self.openIfKeyword, self.openForKeyword)
        ).strip()

        """
        -----------------------------------------------------
        Inicio de Flujos que ocupen una sola Linea
        eg:. if [ condicion ]; then
        ------------------------------------------------------
        """ 
        #Open function statement
        self.oneLineOpenFunction = ("\s*%s\s*\(\s*\)\s*{\s*".strip()
            % (self.var)
        ).strip()

        #First Open if Statement
        self.oneLineOpenIf = ("\s*if\s*\[\s*(%s|%s)\s*\]\s*;\s*then\s*".strip()
            % (self.opCondicional, self.allDataTypes)
        ).strip()

        #Open while statement
        self.oneLineOpenWhile = ("\s*while\s+(%s|\[%s\])\s*;\s*do\s*".strip()
            % (self.boolean, self.opCondicional)
        ).strip()

        #Open for statement
        self.oneLineOpenFor = ("\s*for\s+%s\s+in\s+(%s\s*)+;\s*do\s*".strip()
            % (self.var, self.allDataTypes)
        ).strip()

        #All the multiple line statements
        self.oneLineOpenFlow = ("(%s|%s|%s|%s|%s|%s)".strip() 
            % (self.oneLineOpenFunction, self.oneLineOpenIf, self.openIfKeyword, self.oneLineOpenFor, self.openForKeyword, self.oneLineOpenWhile)
                        ).strip()

        """
        -----------------------------------------------------
        Inicio de Flujos que ocupen 2 Lineas
        eg:. if [ condicion ];
             then
        ------------------------------------------------------
        """

        #Second Open if Statement
        self.twoLinesOpenIf = ("\s*if\s*\[\s*(%s|%s)\s*\]\s*;?\s*".strip()
            % (self.opCondicional, self.allDataTypes)
        ).strip()

        #Two Lines Open For Statement
        self.twoLinesOpenFor = ("\s*for\s+%s\s+in\s+(%s\s*)+".strip()
            % (self.var, self.allDataTypes)
        ).strip()

        #All the Second type multiple line statements
        self.twoLinesOpenFlow = ("(%s|%s)".strip() 
            % (self.twoLinesOpenIf, self.twoLinesOpenFor)
                        ).strip()
        """
        -----------------------------------------------------
        Final de cualquier flujo
        ------------------------------------------------------
        """
        
        #close flow
        self.closeFlow = ("(%s|%s|%s)".strip() 
                    % (self.closeBracket, self.closeIF, self.closeFor)
                        ).strip()

        """
        -----------------------------------------------------
        Sentencias de una sola Linea
        Eg:. echo $hola
        ------------------------------------------------------
        """

        #Impresion
        self.print = ("\s*echo\s*(%s|\s)+\s*".strip()
            % (self.allDataTypes)
        ).strip()

        #Call function
        self.callFunction = ("\s*%s\s*(%s\s*)*".strip()
                    % (self.var, self.allDataTypes)
                            ).strip()
                        
        #One Line Comment //
        self.oneLineComment = "\s*#\s*[^#]*"

        #oneLineStatement
        self.oneLineStatement = ("(%s|%s|%s|%s)".strip()
        % (self.assignment, self.callFunction, self.oneLineComment, self.print)
                        ).strip()

        #One line function
        self.oneLineFunction = ("\s*%s\s*\(\s*\)\s*{\s*((%s)\s*;\s*)*\s*}\s*".strip()
            % (self.var, self.oneLineStatement)
        ).strip()

        

    def isOneLineOpenFlow(self, line):
        return True if re.match("^%s$" % self.oneLineOpenFlow, line) else False

    def isOneLineOpenFunction(self, line):
        return True if re.match("^%s$" % self.oneLineOpenFunction, line) else False

    def isOneLineOpenIf(self, line):
       return True if re.match("^%s$" % self.oneLineOpenIf, line) else False

    def isOneLineOpenWhile(self, line):
        return True if re.match("^%s$" % self.oneLineOpenWhile, line) else False

    def isOneLineOpenFor(self, line):
        return True if re.match("^%s$" % self.oneLineOpenFor, line) else False

    def isTwoLinesOpenFlow(self, line):
        return True if re.match("^%s$" % self.twoLinesOpenFlow, line) else False

    def isOpenKeyword(self, line):
        return True if re.match("^%s$" % self.allOpenKeyword, line) else False        
    
    def isAnyLinesOpenFlow(self, line):
        if(
            self.isOneLineOpenFlow( line ) or
            self.isTwoLinesOpenFlow( line )
        ):
            return True
        else:
            return False
    
    def isOneLineStatement(self, line):
        return True if re.match("^%s$" % self.oneLineStatement, line) else False 
    
    def isCloseFlow(self, line):
        return True if re.match("^%s$" % self.closeFlow, line) else False

    def isOpenComment(self, line):
        return True if re.match("^%s$" % self.openMultipleComment, line) else False

    def isCloseBracket(self, line):
        return True if re.match("^%s$" % self.closeBracket, line) else False

    def isBlank(self, line):
        return True if re.match("^%s$" % self.blank, line) else False

    def getRe(self):
        return self.oneLineOpenWhile
