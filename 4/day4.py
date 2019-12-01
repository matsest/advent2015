import hashlib
import itertools

def bruteForceHash(secret_key):
    sorted_list = map(str,range(1,10000000))
    #for i in itertools.product([str(j) for j in xrange(0,10)], repeat=6):
    #    allNums += [str(j) + ''.join(i) for j in xrange(1,10)]
    
    for item in sorted_list:
#        print "Checking: ", item
#        print "Hash: ", hashlib.md5(secret_key+item).hexdigest()
        if hashlib.md5(secret_key+item).hexdigest().startswith('000000'):
            return item 

part1 = 'bgvyzdsv'
part2 = bruteForceHash(part1)
print "Found:", part2
print "MD5 hash: ", hashlib.md5(part1+part2).hexdigest()
