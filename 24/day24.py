import itertools

row, col = 2978, 3083
M,D = 252533, 33554393
v0 = 20151125

rows =  2*3100 #must be twice the longest dimension you want calculated
cols = rows 

v = [x for x in range(rows*cols)] 

v[0] = v0
for i in range(1,len(v)):
    v[i] = (v[i-1]*M)%D

myArray = [[x for x in range(cols)] for x in range(rows)] #rows*cols array
vi = 0

for diagonalSlice in range(rows + cols -1):
    start_col = max(0, diagonalSlice-rows)
    count = min(diagonalSlice,(cols-start_col),rows) #num of elemens on each diag line
    for j in range(count):
        myArray[min(rows, diagonalSlice)-j-1][start_col+j] = v[vi]
        vi += 1

#print('\n'.join([''.join(['{:10}'.format(item) for item in row[:rows/2]]) for row in myArray[:rows/2][:cols/2]]))

print "koden er i felt 3083,2978 er: "
print myArray[row-1][col-1]
