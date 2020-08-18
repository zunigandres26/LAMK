from tabulate import tabulate
import sys,re

class TabView:

    def __init__(self, lexic, sintactic, semantic):
        self.lexic = lexic
        self.sintactic = sintactic
        self.semantic = semantic

    def print(self):
        repeat = True
        while(repeat):
            print("Selecione que tabla desea ver")
            print("1. Tabla Lexica")
            print("2. Tabla Sintactic")
            print("3. Tabla Semantic")
            print("4. Salir")
            opt = 1
            repeat = False
            if opt == 1:
                self.printLexic(self.lexic)
            elif opt == 2:
                self.printSintactic(self.sintactic)
            elif opt == 3:
                self.printSemantic(self.semantic)
            elif opt == 4:
                print("Cerrando ...")
                repeat = False
            else:
                print("Opcion invalida, acaso eres tonto?")

    def printLexic(self, array):        
        print("1. Lexic Table ")
        print(tabulate(array, headers=["Lexema","Token"], showindex="always", tablefmt="fancy_grid"))
    
    def printSintactic(self, array):        
        print("2. Sintatic Tabled ")
        print(tabulate(array, headers=["Statement","Type"], showindex="always", tablefmt="fancy_grid"))
    
    def printSemantic(self, array):        
        print("3. Semantic Tabled ")
        print(tabulate(array, headers=["Input","Value"], showindex="always", tablefmt="fancy_grid"))
