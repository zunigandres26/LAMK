
from grammars.JSGrammar import *
from grammars.BashGrammar import *
from grammars.RubyGrammar import *

import sys, re

class Verify:

    def __init__(self):
        #Gramaticas de los Lenguajes
        self.jsGrammar = JSGrammar()
        self.bashGrammar = BashGrammar()
        self.rubyGrammar = RubyGrammar()

        #Blank Space
        self.blank = "(\s|\t|\n)*"        

    def isWhatLanguage(self, line):
        if(
            (
            self.bashGrammar.isAnyLinesOpenFlow( line ) or
            self.bashGrammar.isOneLineStatement( line )
            ) and
            (
            self.rubyGrammar.isAnyLinesOpenFlow( line ) or
            self.rubyGrammar.isOneLineStatement( line )
            )
        
        ):
            return 4
        elif(
            self.jsGrammar.isAnyLinesOpenFlow( line ) or
            self.jsGrammar.isOneLineStatement( line )
        ):
            return 1
        elif(
            self.bashGrammar.isAnyLinesOpenFlow( line ) or
            self.bashGrammar.isOneLineStatement( line )
        ):
            return 2
        elif(
            self.rubyGrammar.isAnyLinesOpenFlow( line ) or
            self.rubyGrammar.isOneLineStatement( line )
        ):
            return 3

    def isOneLineOpenFlow(self, line, language):
        if language == 1:
            return self.jsGrammar.isOneLineOpenFlow( line )
        elif language == 2 or language == 4:
            return self.bashGrammar.isOneLineOpenFlow( line )
        elif language == 3:
            return self.rubyGrammar.isOneLineOpenFlow( line )

    def isTwoLinesOpenFlow(self, line, language):
        if language == 1:
            return self.jsGrammar.isTwoLinesOpenFlow( line )
        elif language == 2 or language == 4:
            return self.bashGrammar.isTwoLinesOpenFlow( line )
        if language == 3:
            return self.rubyGrammar.isTwoLinesOpenFlow( line )

    def isOpenKeyword(self, line, language):
        if language == 1:
            return self.jsGrammar.isOpenKeyword( line )
        elif language == 2 or language == 4:
            return self.bashGrammar.isOpenKeyword( line )
        if language == 3:
            return self.rubyGrammar.isOpenKeyword( line )

    def isAnyLinesOpenFlow(self, line, language):
        if(
            self.isOneLineOpenFlow( line, language ) or
            self.isTwoLinesOpenFlow( line, language )
        ):
            return True
        else:
            return False

    def isOneLineStatement(self, line, language):
        if language == 1:
            return self.jsGrammar.isOneLineStatement( line )
        elif language == 2 or language == 4:
            return self.bashGrammar.isOneLineStatement( line )
        elif language == 3:
            return self.rubyGrammar.isOneLineStatement( line )

    def isOpenBracket(self, line, language):
        if language == 1:
            return self.jsGrammar.isOpenBracket( line )
        
    def isCloseFlow(self, line, language):
        if language == 1:
            return self.jsGrammar.isCloseFlow( line )
        elif language == 2 or language == 4:
            return self.bashGrammar.isCloseFlow( line )
        elif language == 3:
            return self.rubyGrammar.isCloseFlow( line )

    def isOpenComment(self, line, language):
        if language == 1:
            return self.jsGrammar.isOpenComment( line )
        elif language == 3:
            return self.rubyGrammar.isOpenComment( line )

    def isCloseComment(self, line, language):
        if language == 1:
            return self.jsGrammar.isCloseComment( line )
        elif language == 3:
            return self.rubyGrammar.isCloseComment( line )

    def isBlank(self, line):
        return True if re.match("^%s$" % self.blank, line) else False
    
    
    def isChangeFlow(self, line, language):
        if language == 1:
            return self.jsGrammar.isChangeFlow( line )
        
    
    def printRe(self):
        print(self.jsGrammar.getRe())

    
