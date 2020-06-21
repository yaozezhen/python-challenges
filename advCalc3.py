# function descriptor: advCalc3()
# advanced calculator that supports addition, subtraction, multiplication, division, and exponentials
# note: input from user does NOT use spaces
#       part 2 of building PEMDAS-based calculator
#       this represents parsing an expression as an algorithm
#       for operations in general, we go "left to right"
#       multiplication and division will come first
#       then the addition and subtraction
#       the example should be parsed as follows:
#           1+2*3*4-2^3  <- input
#           1+2*3*4-8
#           1+6*4-8
#           1+24-8
#           25-8
#           17        <- output
# return type: nothing; program should end when the user types 'n'
# example: Please enter an expression to calculate: '1+2*3*4-2^3'
#          Okay, the output is 17
#          Do you want to calculate anything else? [y|n] 'n'
#          Okay, bye bye :)
# you should start by pasting what you have from part 2
def advCalc3():
  # fill-in code here
  
def add(a,b):
  return a + b
  
def sub(a,b):
  return a - b

def mult(a,b):
  return a * b

def div(a,b): 
  return a / b
  
def exp(a,b):
  return a ** b
