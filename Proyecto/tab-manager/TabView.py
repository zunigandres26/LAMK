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
        print("Lexic Tabled ")
        print(tabulate(array, headers=["Lexema","Token"]))
    
    def printSintactic(self, array):        
        print("Sintatic Tabled ")
        print(tabulate(array, headers=["Statement","Type"]))
    
    def printSemantic(self, array):        
        print("Semantic Tabled ")
        print(tabulate(array, headers=["Input","Value"]))
