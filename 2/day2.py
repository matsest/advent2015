#! /usr/bin/env python
import re

area = 0
ribbon = 0
myFile = open('input.txt','r')
f = list(myFile.readlines())

print "Antall pakker: "
print len(f)

for item in f:
    print "Pakke"
    print(item)
    match = re.findall(r'[\d]{1,2}',item) #find all digits with 1-2 decimals
    match = map(int,match) #convert to int
    print match

    pieces=[match[0]*match[1], match[1]*match[2], match[0]*match[2]]
    sides = sorted([match[0],match[1],match[2]])

    area += 2*sum(pieces) + min(pieces) #all sides + smallest piece for slack
    print area
     

    ribbon += 2*(sides[0]+sides[1]) +sides[0]*sides[1]*sides[2]


print "Total area:"
print area

print "Total ribbon length:"
print ribbon

