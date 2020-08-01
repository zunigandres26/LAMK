# -*- coding:utf-8 -*-

from LexicalAutomata import LexicalAutomata
from Reader import Reader
import sys

text = (Reader()).read()
automata = LexicalAutomata(text).run()

for i in automata.tokens:
    print (i.info())