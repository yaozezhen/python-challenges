# function descriptors: matAdd(m1, m2) matSub(m1, m2) matMult(m1, m2)
# perform respective operations on matricies after checking that dimensions are appropriate
# m1 - matrix 1
# m2 - matrix 2

# matrix addition
def matAdd(m1,m2):
  rows = len(m1)
  cols = len(m1[0])
  if(len(m2) != rows or len(m2[0]) != cols): 
    return "Please double check the dimension of your matrices. "
  output = [[0 for x in range(rows)] for y in range(cols)]
  for i in range(rows): 
    for j in range(cols): 
      output[i][j] = m1[i][j] + m2[i][j]
  return output
  
# matrix subtraction
def matSub(m1,m2):
  rows = len(m1)
  cols = len(m1[0])
  if(len(m2) != rows or len(m2[0]) != cols): 
    return "Please double check the dimension of your matrices. "
  output = [[0 for x in range(rows)] for y in range(cols)]
  for i in range(rows): 
    for j in range(cols): 
      output[i][j] = m1[i][j] - m2[i][j]
  return output

# matrix multiplication
def matMult(m1,m2):
  rows1 = len(m1)
  cols1 = len(m1[0])
  rows2 = len(m2)
  cols2 = len(m2[0])
  if(cols1 != rows2): 
    return "Please double check the dimension of your matrices. "
  output = [[0 for x in range(rows1)] for y in range(cols2)]
  col = 0
  for row in range(rows1): 
    new = 0
    for i in range(cols1): 
      for j in range(rows2): 
        new += m1[row][i] * m2[j][col]
    output[row][col] = new
    col += 1
    if(col == cols2-1):
      col = 0
  return output
  
# create an identity matrix of dimensions n-by-n
def matId(n):
  output = [[0 for x in range(n)] for y in range(n)]
  for i in range(n): 
    for j in range(n): 
      if(i == j): 
        output[i][j] = 1
  return output
  
# some sample matricies you can use to test out your functions
sample1 = [[1,0],[0,1]]
sample2 = [[1,2],[3,4]]
sample3 = [[1,0,0],[0,1,0],[0,0,1]]
sample4 = [[1],[2]]
sample5 = [[0],[1],[2]]

# sample test cases
# matAdd(sample1,sample2)
# matSub(sample1,sample2)
# matMult(sample1,sample4)
# matMult(sample3,sample5)
# matMult(sample3,matId(3))
