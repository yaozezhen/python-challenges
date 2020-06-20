# function descriptor: advCalc2()
# advanced calculator that supports addition, subtraction, and multiplication
# note: input from user does NOT use spaces
#       part 2 of building PEMDAS-based calculator
#       this represents parsing an expression as an algorithm
#       for operations in general, we go "left to right"
#       multiplication will come first
#       then the addition and subtraction
#       the example should be parsed as follows:
#           3*7-4*2+1  <- input
#           21-4*2+1
#           21-8+1
#           14+1
#           15        <- output
# return type: nothing; program should end when the user types 'n'
# example: Please enter an expression to calculate: '3*7-4*2+1'
#          Okay, the output is 7
#          Do you want to calculate anything else? [y|n] 'n'
#          Okay, bye bye :)
# you should start by pasting what you have from part 1
def advCalc2()
  # fill-in code here
  
def add(a,b):
  return a + b
  
def sub(a,b):
  return a - b
  
def mult(a,b):
  return a * b
