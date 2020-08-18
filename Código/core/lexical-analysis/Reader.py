# -*- coding: utf-8 -*-

class Reader: 

    def __init__(self): 
        pass

    def reader(self, fileName):  
        self.text = ""      
        try: 
            f = open(fileName,"r")
            self.text = f.read()
            f.close()

        except EOFError:
            pass 

        return self

    def clean(self, line): 
        return ("%s".strip() % line).strip()