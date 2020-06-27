# function descriptor: advCalc4()
# advanced calculator that supports PEMDAS
# note: input from user does NOT use spaces
#       last part of building PEMDAS-based calculator
#       this represents parsing an expression as an algorithm
#       for operations in general, we go "left to right"
#       things inside parantheses will come first
#       then exponentials
#       then the multiplication and division
#       then the addition and subtraction
#       the example should be parsed as follows:
#           (1+2)*1*(4-2)^3  <- input
#           3*1*(4-2)^3
#           3*1*2^3
#           3*1*8
#           3*8
#           24               <- output
# return type: nothing; program should end when the user types 'n'
# example: Please enter an expression to calculate: '(1+2)*1*(4-2)^3'
#          Okay, the output is 24
#          Do you want to calculate anything else? [y|n] 'n'
#          Okay, bye bye :)
# you should start by pasting what you have from part 3
def advCalc4():
  # fill-in code here
  
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
  
def paran(s):
  return str(eval(s))
