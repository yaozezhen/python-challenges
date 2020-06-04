# function descriptor: gcd(m,n)
# finds the greatest common divisor between two integers
# m - first integer
# n - second integer
# return type: integer
# example: (m,n) - (12, 9) => return 3
def gcd(m,n):
  lsM = [m]
  lsN = [n]
  facM = 1
  facN = 1
  cd = []
  while 2 * facM <= m: 
    if (m % facM == 0):
      lsM.append(facM)
    facM += 1
  while 2 * facN <= n: 
    if (n % facN == 0): 
      lsN.append(facN)
    facN += 1
  for dM in lsM: 
    for dN in lsN: 
      if (dM == dN): 
        cd.append(dM)
  return(max(cd))

print(gcd(12,9))
