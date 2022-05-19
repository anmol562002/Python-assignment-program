from collections import ChainMap

a = {1: 'edureka' , 2: 'python'}
b = {3:'ss' , 4: 'hh'}

al = ChainMap(a,b)
print(al)