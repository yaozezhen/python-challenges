# function descriptor: leastCommon(ls)
# finds the word(s) that shows up the least in a list of strings
# if two or more words show up the same least amount of times, return all of them
# ls - list of strings
# return type: list of strings
# example: ls - ["hello", "hi", "hello"] => return ["hi"]
def leastCommon(ls): 
  strDict = {}
  for i in range(len(ls)): 
    if (ls[i] not in strDict.keys()): 
      strDict[ls[i]] = 1
    else: 
      strDict[ls[i]] += 1
  minFreq = len(strDict)
  outcome = []
  for (key,value) in strDict.items(): 
    if (value <= minFreq): 
      minFreq = value
  for (key,value) in strDict.items(): 
    if (value == minFreq): 
      outcome.append(key)
  return outcome

ls = ["hello","hi","hello"]
print(leastCommon(ls))
