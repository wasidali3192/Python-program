



# Program to multiply two matrices using nested loops
# 3x3 matrix

X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

# 3x4 matrix

Y = [[1,2,3,4],
    [5,6,7,8],
    [9,1,2,3]]

# result is 3x4

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X

for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
