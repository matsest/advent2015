def checkVowels(word,n):
    count = 0
    vowels = ['a','e','i','o','u']
    for letter in vowels:
        if letter in word:
            count += word.count(letter)
    if count >= n:
        return True
    else:
        return False

def checkLettersInRow(word):
    for i in range (0,len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False

def checkForbidden(word):
    forbiddenList = ['ab','cd','pq','xy']
    for item in forbiddenList:
        if item in word:
            return True 
    return False 

def countNiceWords(myList):
    count = 0
    for word in myList:
        if checkVowels(word,3) and checkLettersInRow(word) and not checkForbidden(word):
            count += 1
            print word

    return count

myFile = open('input.txt','r')
f = list(myFile.readlines())
print "Number of words total: ", str(len(f))
print "Number of nice words: ", countNiceWords(f)

