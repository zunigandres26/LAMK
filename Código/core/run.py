# -*- coding:utf-8 -*-

import sys, os
sys.path.insert(0, os.getcwd() + '/core/lexical-analysis')
sys.path.insert(0, os.getcwd() + '/core/sintax-analysis')
sys.path.insert(0, os.getcwd() + '/core/semantic-analysis')

from Automata import Automata
import re
import subprocess
from Semantic import Semantic
from lark import Lark,Transformer
from Grammar import *
from Reader import Reader
from SyntaxAnalyzer import SyntaxAnalyzer
from tabulate import tabulate


class execute:

    def __init__(self, parameters):
        self.parameters = parameters

    def run(self):
        if len(self.parameters) > 1:
            if len(self.parameters) == 3:                
                if self.parameters[1] == "--exec":
                    self.exec(self.parameters[2])
                elif self.parameters[1] == "--tabview":
                    self.tabview(self.parameters[2])  
                elif self.parameters[1] == "--recognize":
                    self.recognize(self.parameters[2])  
                else:
                    print("Comando no soportado o desconocido")
                    self.help()         
            elif len(self.parameters) == 2:
                if self.parameters[1] == "--info":
                    self.info()      
                elif self.parameters[1] == "--help":
                    self.help()
                else: 
                    print("Comando no soportado o desconocido")
                    self.help()
            else:
                print("Comando no soportado o desconocido")
                self.help()
        else:
            self.help()
    
    def exec(self, filename):
        # Ejecución del analizador Léxico
        reader = (Reader()).reader(filename)
        automata = (Automata(reader)).run()
        
        # Ejecución del analizador Sintáctico
        sintactic = (SyntaxAnalyzer(reader).run())

        # Ejecución del analizador Semántico
        transformer = Semantic()
        parser = Lark(grammar,parser="lalr",lexer="contextual",transformer = transformer)
        language = parser.parse

        try:
            language(sintactic.getCode(sintactic.statements))
        except Exception as e:
            print ("Error: %s" % e)


    def recognize(self, filename):
        reader = (Reader()).reader(filename)
        sintactic = (SyntaxAnalyzer(reader).run())
        print("Se ha reconocido al Lenguaje %s" % sintactic.getLanguage( sintactic.language ))
        print("\n\nEl código leído es:\n",sintactic.getCode(sintactic.statements))
    
    def tabview(self, filename):
        reader = (Reader()).reader(filename)
        sintactic = (SyntaxAnalyzer(reader).run())
        code = sintactic.preprocess(sintactic.statements)
        cleanCode = sintactic.clean(code)
        
        transformer = Semantic()
        parser = Lark(grammar,parser="lalr",lexer="contextual",transformer = transformer)
        language = parser.parse

        self.blockPrint()

        try:
            language(sintactic.getCode(sintactic.statements))
            result = transformer.tablita(cleanCode)
        except Exception as e:
            print ("Error: %s" % e)

        self.enablePrint()
        print(tabulate(result, headers=["#","Lexema","Token","Initial Value","Final Value"], showindex="always", tablefmt="fancy_grid"))

    def help(self):
        print("Bienvenido a la utilidad de ayuda de LIR 1.0\n")
        print("Ejecutar el programa                  --exec fileName")
        print("Muestra la tabla de simbolos          --tabview fileName")
        print("Muestra la tabla de simbolos          --recognize fileName")
        print("Muestra la informacion del programa   --info")
        print("Comandos soportados                   --help")
    
    def info(self):
        print("*"*45)
        print("* Interprete LRI", " "*26, "*\n*"," "*41, "*")
        print("* @author Alexis Daniel Ochoa   20161002139 *")
        print("* @author Andres Alberto Zuniga 20161003850 *")
        print("* @author Marco Tulio Ruiz      20171006559 *")
        print("* @author Kenneth Leonel Cruz   20141010391 *\n*"," "*41, "*")
        print("* @version Released Version 1.0", " "*11, "*" )
        print("* @date 2020-08-17", " "*24, "*")
        print("*"*45)

    def blockPrint(self):
        sys.stdout = open(os.devnull, 'w')

    def enablePrint(self):
        sys.stdout = sys.__stdout__

"""
reader = (Reader()).reader()


values = []
for i in automata.tokens:
    values.append(i.info())

tv = TabView(values, values, values)
tv.print()

parser = Lark(grammar,parser="lalr",lexer="contextual",transformer = Semantic())
language = parser.parse



sample = reader.text
try:
    language(code)
except Exception as e:
    print ("Error: %s" % e)
"""