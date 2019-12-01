#!/usr/bin/env python

from numpy import ushort
from itertools import product
from string import ascii_lowercase

myFile = open('input.txt','r')
f = myFile.readlines()

keys = [''.join(i) for i in product(ascii_lowercase,repeat = 2)]
for i in ascii_lowercase: keys.append(i)

wires = {key: 0 for key in keys}
wires['a'] = 5
print wires['a'] & wires['bh']

for line in f[:10]:
    line = line.split()
    line.reverse()
    print line
# må ha pekere?
'''
    if 'AND' in line:
        dict[line[0]] = line[4] & line[2]
    elif 'OR' in line:
        dict[line[0]] = line[4] | line[2]
    elif 'RSHIFT' in line:
        dict[line[0]] = line[4] | line[2]
    elif 'LSHIFT' in line:
        dict[line[0]] = line[4] | line[2]
    elif 'NOT' in line:
        dict[line[0]] = line[2]
    else:
        dict[line[0]] = line[2]

'''
