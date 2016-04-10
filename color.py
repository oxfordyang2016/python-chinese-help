

#coding utf-8
from   xtermcolor import colorize
import platform 
import random
if platform.system()=='windows':
    string=unicode(string,'utf-8')
def cp(string):

    print(colorize(string,ansi=random.randint(1,200)))
