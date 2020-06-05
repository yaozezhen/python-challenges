# function descriptor: removeNums(s)
# removes numbers from a given string
# s - a string that only contains alphanumeric characters
# return type: string
# example: s - "Hel1o" => return "Helo"
def removeNums(s):
  ls = []
  output = []
  for char in s: 
    ls.append(ord(char))
  for num in ls: 
    if (num > 64): 
      output.append(chr(num))
  return "".join(output)

print(removeNums("Hel1o"))
