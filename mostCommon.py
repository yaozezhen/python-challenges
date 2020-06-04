# function descriptor: mostCommon(ls)
# finds the word(s) that shows up the most in a list of strings
# if two or more words show up the same amount of times, return all of them
# ls - list of strings
# return type: list of strings
# example: ls - ["hello", "hi", "hello"] => return ["hello"]
def mostCommon(ls): 
  strDict = {}
  for i in range(len(ls)): 
    if (ls[i] not in strDict.keys()): 
      strDict[ls[i]] = 1
    else: 
      strDict[ls[i]] += 1
  maxFreq = 1
  outcome = []
  for (key,value) in strDict.items(): 
    if (value >= maxFreq): 
      maxFreq = value
  for (key,value) in strDict.items(): 
    if (value == maxFreq): 
      outcome.append(key)
  return outcome

ls = ["hello","hi","hello","hi"]
print(mostCommon(ls))
