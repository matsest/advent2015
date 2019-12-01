#! /usr/bin/env python

floor = 0;
myFile = open('day1in.txt','r')
f = list(myFile.read())

#printe lista
#print f

print "Antall instrukser: "
print len(f)

opp = f.count("(")
ned = f.count(")")

floor = opp - ned

print "Antall opp: " + str(opp)
print "Antall ned: " + str(ned)
print "Ender pa etasje: "
print floor

etg = 0
for i in range(1,len(f)):
    if f[i-1] == "(":
        etg += 1
        print "i etasje", etg
    elif f[i-1] == ")":
        etg -= 1
        print "i etasje", etg
    if etg == -1:
        break
print "I kjeller pa posisjon ", i
