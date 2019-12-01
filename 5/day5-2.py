def checkNotOverlap(word):
    print word
    for i in range(len(word)-1):
        pair = (word[i], word[i+1])
        for j in range(i+2,len(word)-1):
            match = (word[j],word[j+1])
            if pair == match:
                return True
    return False

def checkSeparation(word):
    for i in range(len(word)-2):
        if word[i] == word[i+2]:
            return True

def countNiceWords(myList):
    count = 0
    for word in myList:
        if checkSeparation(word) and checkNotOverlap(word):
            count += 1
            print word
    return count

myFile = open('input.txt','r')
f = list(myFile.readlines())
print "Number of words total: ", str(len(f))
print "Number of nice words: ", countNiceWords(f)
