# -*- coding:utf-8 -*-

import sys, os
sys.path.insert(0, os.getcwd() + '/core')
from run import *

run = execute(sys.argv)
run.run()