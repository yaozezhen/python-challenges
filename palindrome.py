# function descriptor: palindrome(s)
# checks if the string input is a palindrome (same string when reversed)
# s - string to be checked
# return type: boolean
# example: s - "racecar" => return True
#          s - "abcdca" => return False
def palindrome(s):
  l = len(s)
  b = True
  for i in range(int(l/2)): 
    if(s[i] != s[l-i-1]): 
      b = False
      break
  return b

print(palindrome("wow"))
