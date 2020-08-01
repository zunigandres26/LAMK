# -*- coding: utf-8 -*-

class Token: 

    def __init__(self): 
        self.code = 0
        self.type = ""
        self.value = []
        self.formed = False
        self.inFormation = False 

    def add(self, char): 
        self.value += [char]

    def atFirst(self): 
        return None if len(self.value) == 0 else  self.value[0]

    def info(self): 
        return (
            "".join( list((map( lambda x: chr(x), self.value ))) ), 
            self.type
        )