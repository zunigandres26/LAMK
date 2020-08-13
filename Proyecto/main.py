import sys, os
sys.path.insert(0, os.getcwd() + '/lexical-analysis')
sys.path.insert(0, os.getcwd() + '/sintax-analysis')
sys.path.insert(0, os.getcwd() + '/semantic-analysis')

from Automata import Automata
import sys
from Semantic import Semantic
from lark import Lark,Transformer
from Grammar03 import *
from Reader import Reader
from SyntaxAnalyzer import SyntaxAnalyzer

reader = (Reader()).reader()
#automata = (Automata(reader)).run()

#[print( i.info() ) for i in automata.tokens ]


sintactic = (SyntaxAnalyzer(reader).run())

print("Se ah reconocido al Lenguaje %s" % sintactic.getLanguage( sintactic.language ))

"""for i in sintactic.statements:
    print()
    print("-"*50)
    print("%s encontrado" % i.type)
    print("-"*50)
    print(i.lines)
    print()
"""
"""
parser = Lark(grammar,parser="lalr",lexer="contextual",transformer = Semantic())
language = parser.parse

sample = reader.text
try:
    language(sample)
except Exception as e:
    print ("Error: %s" % e)
"""