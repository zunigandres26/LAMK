import sys, os
sys.path.insert(0, os.getcwd() + '/lexical-analysis')
sys.path.insert(0, os.getcwd() + '/sintax-analysis')

from Automata import Automata
from Reader import Reader
from SyntaxAnalyzer import SyntaxAnalyzer

reader = (Reader()).reader()
#automata = (Automata(reader)).run()

#[print( i.info() ) for i in automata.tokens ]

sintactic = (SyntaxAnalyzer(reader).run())

for i in sintactic.statements:
    print()
    print("-"*50)
    print("%s encontrado" % i.type)
    print("-"*50)
    print(i.lines)
    print()
