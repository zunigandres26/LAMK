# -*- coding: utf-8 -*-

class Reader: 

    def __init__(self): pass

    def reader(self):
        self.text = []

        try: 
            text = input()
            while True: 
                self.text += [ self.clean(text) ]
                text = input()

        except EOFError:
            pass 

        self.text = "\n".join( self.text )

        return self

    def clean(self, line): 
        return ("%s".strip() % line).strip()