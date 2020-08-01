import sys, os
sys.path.insert(0, os.getcwd() + '/lexical-analysis')

from Automata import Automata
from Reader import Reader

reader = (Reader()).reader()
automata = (Automata(reader)).run()

[print( i.info() ) for i in automata.tokens ] 