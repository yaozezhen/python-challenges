# function descriptor: nextPrime(n)
# find the next prime number after the input value
# n - positive integer
# return type: integer
# example: n - 12 => return 13
def checkPrime(n): 
  p = 2
  while p*p <= n: 
    if (n % p == 0):
      return False
    p += 1
  return True

def nextPrime(n):
  num = n+1
  while True: 
    if(checkPrime(num) == True): 
      break
    num += 1
  return num

print(nextPrime(13))
