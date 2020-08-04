import re

class Verify:

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
                            % (self.var, self.number)
                        )

        #Open if Statement
        self.openIf = ("\s*if\s*\(%s\)\\s*{\s*".strip() % self.opCondicional).strip()

        #Params
        self.params = ("\s*%s\s*\,?\s*(%s)?\s*" % (self.var, self.var))
        
        #Open function statement
        self.openFunction = ("\s*function\s+%s\s*\(%s\)\s*{\s*".strip()
            % (self.var, self.params)
        ).strip()

        #Open while statement
        self.openWhile = ("\s*while\s*\((%s|\s*%s\s*)\)\s*{\s*".strip()
                            % (self.opCondicional, self.boolean)
                        )

        #Open for statement
        self.openFor = ("\s*for\s*\(%s;%s;\s*(%s)\s*\)\s*{\s*".strip()
                            % (self.intAssignment, self.opCondicional, self.counters)
                        )

        #Open multiple comments
        self.openMultipleComment = ("\s*\/\*\s*[^\/\*]*\s*")

        #All the multiple line statements
        self.openFlow = ("(%s|%s|%s|%s|%s)".strip() 
            % (self.openFor, self.openFunction, self.openIf, self.openWhile, self.openMultipleComment)
                        )

        #Close Bracket
        self.closeBracket = "\s*}\s*"

        #Close Comments
        self.closeComment = "\s*[^\*\/]*\s*\*\/\s*"

        #close flow
        self.closeFlow = ("(%s|%s)".strip() 
                    % (self.closeBracket, self.closeComment)
                        ).strip()

        #Blank Space
        self.blank = "(\s|\t|\n)*"

        #Param function
        self.paramFunction = ("\s*%s.?%s?\(\s*%s\s*\)\s*".strip()
                    % (self.var, self.var, self.var)
                            )

        #Call Function Params
        self.callParams = ("\s*(%s|%s)?\s*\,?\s*(%s|%s)?\s*".strip()
                    % (self.allDataTypes, self.paramFunction, self.allDataTypes, self.paramFunction)
                        )

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

    

    def isOpenFunction(self, line):
        return True if re.match("^%s$" % self.openFunction, line) else False

    def isOpenFlow(self, line):
        return True if re.match("^%s$" % self.openFlow, line) else False

    def isCloseFlow(self, line):
        return True if re.match("^%s$" % self.closeFlow, line) else False

    def isOpenIf(self, line):
        return True if re.match("^%s$" % self.openIf, line) else False

    def isOpenWhile(self, line):
        return True if re.match("^%s$" % self.openWhile, line) else False

    def isOpenFor(self, line):
        return True if re.match("^%s$" % self.openFor, line) else False

    def isOpenComment(self, line):
        return True if re.match("^%s$" % self.openMultipleComment, line) else False

    def isCloseBracket(self, line):
        return True if re.match("^%s$" % self.closeBracket, line) else False

    def isBlank(self, line):
        return True if re.match("^%s$" % self.blank, line) else False

    def isOneLineStatement(self, line):
        return True if re.match("^%s$" % self.oneLineStatement, line) else False 
    
    def printRe(self):
        print(self.openWhile)
