# function descriptor: alphabetSort(s)
# sorts the letters in the string given
# s - a string that only contains letters
# return type: string
# example: s - "happy" => return "ahppy"
def alphabetSort(s):
  ls1 = []
  ls2 = []
  for letter in s: 
    ls1.append(ord(letter))
  while True: 
    ls2.append(chr(min(ls1)))
    ls1.remove(min(ls1))
    if(len(ls1) == 0): 
      break
  return "".join(ls2)

print(alphabetSort("tessellation"))
