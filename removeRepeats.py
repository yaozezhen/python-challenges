# function descriptor: removeRepeats(s)
# removes repeated characters from a string and returns the result
# s - a string that contains characters from the ASCII table
# return type: string
# example: s - "abc89c ba90* +*" => return "abc89 0*+"
def removeRepeats(s):
  l = []
  for item in s: 
    if item not in l: 
      l.append(item)
  return "".join(l)

print(removeRepeats("abc89c ba90* +*"))
