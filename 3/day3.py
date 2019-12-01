#! /usr/bin/env python

myFile = open('input.txt','r')
f = list(myFile.read())

fSanta = f[0::2]
fRobo = f[1::2]

x = 0
y = 0
myCoord = (x,y)
houses = [myCoord]

print "Ordentlig nisse:"
for direction in fSanta:
    if direction == "^":
        y += 1
    elif direction == "v":
        y -= 1
    elif direction == "<":
        x -= 1
    elif direction == ">":
        x += 1

    myCoord = (x,y)
    print direction
    print myCoord
    if myCoord not in houses:
        houses.append(myCoord)
        print "Ny adresse"
    else:
        print "Allerede besokt"

print "Robotnisse:"
x = 0
y = 0
for direction in fRobo:
    if direction == "^":
        y += 1
    elif direction == "v":
        y -= 1
    elif direction == "<":
        x -= 1
    elif direction == ">":
        x += 1

    myCoord = (x,y)
    print direction
    print myCoord
    if myCoord not in houses:
        houses.append(myCoord) 
        print "Ny adresse"
    else:
        print "Allerede besokt"

print "Hus som far minst en gave"
print len(houses)


