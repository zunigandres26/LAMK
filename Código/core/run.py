# -*- coding:utf-8 -*-

import sys, os
sys.path.insert(0, os.getcwd() + '/core/lexical-analysis')
sys.path.insert(0, os.getcwd() + '/core/sintax-analysis')
sys.path.insert(0, os.getcwd() + '/core/semantic-analysis')
sys.path.insert(0, os.getcwd() + '/core/tab-manager')

from Automata import Automata
import re
from Semantic import Semantic
from lark import Lark,Transformer
from Grammar import *
from TabView import TabView
from Reader import Reader
from SyntaxAnalyzer import SyntaxAnalyzer


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
        reader = (Reader()).reader(filename)
        automata = (Automata(reader)).run()

    def recognize(self, filename):
        reader = (Reader()).reader(filename)
        sintactic = (SyntaxAnalyzer(reader).run())
        print("Se ha reconocido al Lenguaje %s" % sintactic.getLanguage( sintactic.language ))
        print("\n\nEl código leído es:\n",sintactic.getCode(sintactic.statements))
    
    def tabview(self, filename):
        print("Alex aun nada sabe de python")

    def help(self):
        print("comandos soportados\n")
        print("Ejecutar el programa                  --exec fileName")
        print("Muestra la tabla de simbolos          --tabview fileName")
        print("Muestra la tabla de simbolos          --recognize fileName")
        print("Muestra la informacion del programa   --info")
        print("Comandos soportados                   --help")
    
    def info(self):
        print("*"*45)
        print("* Interprete:", " "*29, "*\n*"," "*41, "*")
        print("* @author Alexis Daniel Ochoa   20161002139 *")
        print("* @author Andres Alberto Zuniga 20161003850 *")
        print("* @author Marco Tulio Ruiz      20171006559 *")
        print("* @author Kenneth Leonel Cruz   20141010391 *\n*"," "*41, "*")
        print("* @version Released Version 1.0", " "*11, "*" )
        print("* @date 2020-08-17", " "*24, "*")
        print("*"*45)

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