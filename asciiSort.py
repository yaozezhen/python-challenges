# function descriptor: asciiSort(s)
# sorts the letters in the string given
# s - a string that contains characters from the ASCII table
# return type: string
# example: s - "k9A* =1>c+" => return "*+19=>Ack "
def asciiSort(s):
  ls = []
  outcome = []
  for letter in s:
    ls.append(ord(letter))
  while True: 
    outcome.append(chr(min(ls)))
    ls.remove(min(ls))
    if(len(ls) == 0): 
      break
  return "".join(outcome)

print(asciiSort("k9A* =1>c+"))
