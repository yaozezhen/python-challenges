import math
# function descriptor: circleCalc(r)
# calculates circle measures
# return type: nothing; program should end when the user types 'n'
# example: Today we will be finding the different measures a circle gives us.
#          What would you like the radius to be? '2'
#          The radius of the circle you chose is 2.
#          What would you like to calculate? [area|circumference] 'area'
#          Okay, the area is ___
#          Do you want to calculate anything else? [y|n] 'y'
#          What would you like to calculate? [area|circumference] 'circumference'
#          Okay, the circumference is ___
#          Do you want to calculate anything else? [y|n] 'n'
#          Okay, bye bye :)
def circleCalc():
  print("Today we will be finding the different measures a circle gives us.")
  while True: 
    r = input("What would you like the radius to be? ")
    if (float(r) <= 0): 
      print("Choose a positive number. ")
    else: 
      break
  while True: 
    measurement = input("What would you like to calculate? [A: area| B: circumference] ")
    if(measurement == "A"): 
      a = round(math.pi * float(r) * float(r), 2)
      print("Okay, the area is " + str(a))
    if(measurement == "B"): 
      c = round(2 * math.pi * float(r), 2)
      print("Okay, the circumference is " + str(c))
    more = input("Do you want to calculate anything else? [Y|N] ")
    if (more == "N"): 
      break
  print("Okay, bye :)")
  return 

circleCalc()
