import sys, os
sys.path.insert(0, os.getcwd() + '/lexical-analysis')
sys.path.insert(0, os.getcwd() + '/sintax-analysis')
sys.path.insert(0, os.getcwd() + '/semantic-analysis')

from Automata import Automata
import sys,re
from Semantic import Semantic
from lark import Lark,Transformer
from Grammar03 import *
from Reader import Reader
from SyntaxAnalyzer import SyntaxAnalyzer

reader = (Reader()).reader()
#automata = (Automata(reader)).run()

#[print( i.info() ) for i in automata.tokens ]

"""
sintactic = (SyntaxAnalyzer(reader).run())

#print("Se ah reconocido al Lenguaje %s" % sintactic.getLanguage( sintactic.language ))


code = sintactic.getCode(sintactic.statements)
print( code )

"""
parser = Lark(grammar,parser="lalr",lexer="contextual",transformer = Semantic())
language = parser.parse

sample = reader.text
try:
    language(sample)
except Exception as e:
    print ("Error: %s" % e)
