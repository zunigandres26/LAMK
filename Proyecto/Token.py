# -*- coding: utf-8 -*-

import re

class Token:

    def __init__(self):
        self.formed = False
        self.inFormation = False
        self.value = []
        self.type = None
        self.tokenCode = None
        
    def add(self, value):
        self.value += [value]

    def info(self):
        return (
            "".join(list(map(lambda x: chr(x),self.value))),
            self.type
        )

    
