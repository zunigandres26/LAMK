class Statement:

    def __init__(self):
        self.lines = []
        self.InAnalysis = False
        self.analyzed = False
        self.type = ""
        self.forClose = 0

    def add(self, line):
        self.lines += [line]

    def atFirst(self): 
        return None if len(self.lines) == 0 else  self.lines[0]

    def info(self): 
        return (
            "".join( list((map( lambda x: chr(x), self.lines ))) ), 
            self.type
        )