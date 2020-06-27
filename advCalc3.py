# function descriptor: advCalc3()
# advanced calculator that supports addition, subtraction, multiplication, division, and exponentials
# note: input from user does NOT use spaces
#       part 2 of building PEMDAS-based calculator
#       this represents parsing an expression as an algorithm
#       for operations in general, we go "left to right"
#       exponentials will come first
#       then the multiplication and division
#       then the addition and subtraction
#       the example should be parsed as follows:
#           1+2*3*4-2^3  <- input
#           1+2*3*4-8
#           1+6*4-8
#           1+24-8
#           25-8
#           17           <- output
# return type: nothing; program should end when the user types 'n'
# example: Please enter an expression to calculate: '1+2*3*4-2^3'
#          Okay, the output is 17
#          Do you want to calculate anything else? [y|n] 'n'
#          Okay, bye bye :)
# you should start by pasting what you have from part 2
def advCalc3():
  while True: 
    expression = input("Please enter and expression to calculate: ")
    ls = []
    numLs = []
    oprLs = []
    current = 0
    lastNum = []
    for item in expression: 
      ls.append(item)
    for i in range(len(ls)): 
      if(ls[i] == "+" or ls[i] == "-" or ls[i] == "*" or ls[i] == "/" or ls[i] == "^"): 
        oprLs.append(ls[i])
        num = []
        lastOpr = i
        for j in range(current,i): 
          num.append(ls[j])
        numLs.append("".join(num))
        current = i+1
    for i in range(lastOpr+1, len(ls)): 
      lastNum.append(ls[i])
    numLs.append("".join(lastNum))
    while True: 
      for i in range(len(oprLs)): 
        if(oprLs[i] == "+" or oprLs[i] == "-" or oprLs[i] == "*" or oprLs[i] == "/"): 
          continue
        if(oprLs[i] == "^"): 
          newNum = expo(int(numLs[i]), int(numLs[i+1]))
        oprLs.pop(i)
        numLs.pop(i+1)
        numLs.pop(i)
        numLs.insert(i, newNum)
        break
      checkExpo = 0
      for i in range(len(oprLs)): 
        if(oprLs[i] == "+" or oprLs[i] == "-" or oprLs[i] == "*" or oprLs[i] == "/"): 
          checkExpo += 1
      if(checkExpo == len(oprLs)): 
        break
    while True: 
      for i in range(len(oprLs)): 
        if(oprLs[i] == "+" or oprLs[i] == "-"): 
          continue
        if(oprLs[i] == "*"): 
          newNum = mult(int(numLs[i]), int(numLs[i+1]))
        if(oprLs[i] == "/"): 
          newNum = div(int(numLs[i]), int(numLs[i+1]))
        oprLs.pop(i)
        numLs.pop(i+1)
        numLs.pop(i)
        numLs.insert(i, newNum)
        break
      checkMD = 0
      for i in range(len(oprLs)): 
        if(oprLs[i] == "+" or oprLs[i] == "-"): 
          checkMD += 1
      if(checkMD == len(oprLs)): 
        break
    while True: 
      for i in range(len(oprLs)): 
        if(oprLs[i] == "+"): 
          newNum = add(int(numLs[i]), int(numLs[i+1]))
        if(oprLs[i] == "-"): 
          newNum = sub(int(numLs[i]), int(numLs[i+1]))
        oprLs.pop(i)
        numLs.pop(i+1)
        numLs.pop(i)
        numLs.insert(i, newNum)
        break
      if(len(oprLs) == 0):
        break
    print("Okay, the output is " + str(numLs[0]))
    more = input("Do you want to calculate anything else? [y|n] ")
    if(more == "n"): 
      print("Okay, bye bye :)")
      break
  return
  
def add(a,b):
  return a + b
  
def sub(a,b):
  return a - b

def mult(a,b):
  return a * b

def div(a,b): 
  return a / b

def expo(a,b): 
  return a ** b

advCalc3()
