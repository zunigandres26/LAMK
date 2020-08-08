
import re
"""
--------------------------------------------------------
Clase Gramatica del Lenguaje de Programacion Javascript
--------------------------------------------------------
"""
class JSGrammar:

    def __init__(self):
         
        #Variables
        self.var = "[A-Za-z][A-Za-z0-9]*"

        #Data Types
        self.string = "(\"[^\"]*\"|'[^']*')"
        self.number = "[0-9]+"
        self.boolean = "(true|false)"

        #Variables and Data Types
        self.allDataTypes = ("(%s|%s|%s|%s)".strip() 
            % (self.var, self.string, self.number, self.boolean)
                            )

        #Operators
        self.operators = "==|>|>=|<|<="

        #Counters
        self.counters = ("%s\+\+|%s\-\-".strip() % (self.var, self.var))

        #Conditional
        self.opCondicional = ("\s*(%s|%s)\s*(%s)\s*(%s|%s)\s*".strip()
                            % (self.var, self.number, self.operators, self.var, self.number)
                        ).strip()

        #var assignment
        self.assignment = ("\s*%s\s*=\s*(%s|%s|%s|%s)\s*;?\s*".strip()
                    % (self.var, self.number, self.string, self.var, self.boolean)
                        )

        #Integer Only Assignment
        self.intAssignment = ("\s*%s\s*=\s*%s\s*".strip()
                            % (self.var, self.number))
        #Params
        self.params = ("\s*%s\s*\,?\s*(%s)?\s*" % (self.var, self.var))


        #Open Bracket
        self.openBracket = "\s*{\s*"

        #all open flow keyword
        self.allOpenKeyword = ("(%s)".strip()
            % (self.openBracket)
        ).strip()
        
        #Close Bracket
        self.closeBracket = "\s*}\s*"

        #Close Comments
        self.closeComment = "\s*[^\*\/]*\s*\*\/\s*"

        #Blank Space
        self.blank = "(\s|\t|\n)*"


        #Open multiple comments
        self.openMultipleComment = ("\s*\/\*\s*[^\/\*]*\s*")

        #Param function
        self.paramFunction = ("\s*%s.?%s?\(\s*%s\s*\)\s*".strip()
                    % (self.var, self.var, self.var)
                            )

        #Call Function Params
        self.callParams = ("\s*(%s|%s)?\s*\,?\s*(%s|%s)?\s*".strip()
                    % (self.allDataTypes, self.paramFunction, self.allDataTypes, self.paramFunction)
                        )
        
        """
        -----------------------------------------------------
        Inicio de flujos que solo ocupen 1 Linea
        Eg:. if (condicion) {
        ------------------------------------------------------
        """                

        #Open if Statement
        self.oneLineOpenIf = ("\s*if\s*\(%s\)\\s*{\s*".strip() % self.opCondicional).strip()

        #Open function statement
        self.oneLineOpenFunction = ("\s*function\s+%s\s*\(%s\)\s*{\s*".strip()
            % (self.var, self.params)
        ).strip()

        #Open while statement
        self.oneLineOpenWhile = ("\s*while\s*\((%s|\s*%s\s*)\)\s*{\s*".strip()
                            % (self.opCondicional, self.boolean)
                        )
        
        #Open for statement
        self.oneLineOpenFor = ("\s*for\s*\(\s*(var)?%s;%s;\s*(%s)\s*\)\s*{\s*".strip()
                            % (self.intAssignment, self.opCondicional, self.counters)
                        )

        #All the multiple line statements
        self.oneLineOpenFlow = ("(%s|%s|%s|%s|%s|%s)".strip() 
            % (self.oneLineOpenFor, self.oneLineOpenFunction, self.oneLineOpenIf, self.oneLineOpenWhile, self.openMultipleComment, self.openBracket)
                        )

        """
        -----------------------------------------------------
        Inicio de flujos que ocupen 2 Lineas
        Eg:. if (condicion) 
             {
        ------------------------------------------------------
        """                

        #Second if statement
        self.twoLinesOpenIf = ("\s*if\s*\(%s\)\s*".strip() % self.opCondicional).strip()
        
        
        #Second open function statement
        self.twoLinesOpenFunction = ("\s*function\s+%s\s*\(%s\)\s*".strip()
            % (self.var, self.params)
        ).strip()
        


        #Second open while statement
        self.twoLinesOpenWhile = ("\s*while\s*\((%s|\s*%s\s*)\)\s*".strip()
                            % (self.opCondicional, self.boolean)
                        )

        #Second Open for statement
        self.twoLinesOpenFor = ("\s*for\s*\(\s*(var)?%s;%s;\s*(%s)\s*\)\s*".strip()
                            % (self.intAssignment, self.opCondicional, self.counters)
                        )

        #Second Open Flow
        self.twoLinesOpenFlow = ("(%s|%s|%s|%s)".strip()
            % (self.twoLinesOpenIf, self.twoLinesOpenFunction, self.twoLinesOpenWhile, self.twoLinesOpenFor)
        ).strip()

        """
        -----------------------------------------------------
        Final de Cualquier Flujo
        ------------------------------------------------------
        """
  
        #close flow
        self.closeFlow = ("(%s|%s)".strip() 
                    % (self.closeBracket, self.closeComment)
                        ).strip()

        """
        -----------------------------------------------------
        Sentencias de una sola Linea
        Eg:. if(condicion) return true
        ------------------------------------------------------
        """
        #Call function
        self.callFunction = ("\s*%s.?%s?\(%s\)\s*;?\s*".strip()
                    % (self.var, self.var, self.callParams)
                            )

        #if One Line
        self.ifOneLine = ("\s*if\s*\(%s\)\s*return\s*%s\s*;?\s*".strip()
            % (self.opCondicional, self.allDataTypes)
                        )
        #return
        self.returnAll = "\s*return\s*[A-Za-z0-9\+\-\/\*\(\)\s]+\s*;?\s*"

        #One Line Comment //
        self.oneLineComment = "\s*\/\/\s*[^/]*\s*"

        #oneLineStatement
        self.oneLineStatement = ("(%s|%s|%s|%s|%s)".strip()
        % (self.returnAll, self.assignment, self.callFunction, self.ifOneLine, self.oneLineComment)
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

    def isCloseComment(self, line):
        return True if re.match("^%s$" % self.closeComment, line) else False

    def isCloseBracket(self, line):
        return True if re.match("^%s$" % self.closeBracket, line) else False

    def isOpenBracket(self, line):
        return True if re.match("^%s$" % self.openBracket, line) else False

    def isBlank(self, line):
        return True if re.match("^%s$" % self.blank, line) else False
    
    def getRe(self):
        return self.oneLineOpenFor 
