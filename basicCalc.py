# function descriptor: basicCalc()
# basic calculator based on user input
# return type: nothing; program should end when the user types 'n'
# example: Today we will be performing basic arithmetic on two numbers
#          What would operation would you like to perform? [add|sub|mult] 'add'
#          The operation you chose was addition.
#          Enter two numbers to find the sum: '2 5'
#          Okay, the sum is 7
#          What would operation would you like to perform? [add|sub|mult] 'sub'
#          The operation you chose was subtraction.
#          Enter two numbers to find the difference: '2 5'
#          Okay, the difference is -3
#          Do you want to calculate anything else? [y|n] 'n'
#          Okay, bye bye :)
def basicCalc():
  print("Today we will be performing basic arithmetic on two numbers. ")
  while True: 
    operation = input("What would operation would you like to perform? [add|sub|mult] ")
    if (operation == "add"): 
      print("The operation you chose was addition.")
      num = input("Enter two numbers to find the sum: ")
      ls = []
      for i in num: 
        ls.append(i)
      ls1 = []
      ls2 = []
      for i in range(len(ls)): 
        if (ls[i] == " "):
          for j in range(i): 
            ls1.append(ls[j])
          for j in range(i+1,len(ls)): 
            ls2.append(ls[j])
      num1 = int("".join(ls1))
      num2 = int("".join(ls2))
      print("Okay, the sum is " + str(num1+num2) + " .")
    if (operation == "sub"): 
      print("The operation you chose was subtraction.")
      num = input("Enter two numbers to find the difference: ")
      ls = []
      for i in num: 
        ls.append(i)
      ls1 = []
      ls2 = []
      for i in range(len(ls)): 
        if (ls[i] == " "):
          for j in range(i): 
            ls1.append(ls[j])
          for j in range(i+1,len(ls)): 
            ls2.append(ls[j])
      num1 = int("".join(ls1))
      num2 = int("".join(ls2))
      print("Okay, the difference is " + str(num1-num2) + " .")
    if (operation == "mult"): 
      print("The operation you chose was multiplication.")
      num = input("Enter two numbers to find the product: ")
      ls = []
      for i in num: 
        ls.append(i)
      ls1 = []
      ls2 = []
      for i in range(len(ls)): 
        if (ls[i] == " "):
          for j in range(i): 
            ls1.append(ls[j])
          for j in range(i+1,len(ls)): 
            ls2.append(ls[j])
      num1 = int("".join(ls1))
      num2 = int("".join(ls2))
      print("Okay, the product is " + str(num1*num2) + " .")
    more = input("Do you want to calculate anything else? [y|n] ")
    if (more == "n"): 
      break
  print("Okay, bye. ")
  return 

basicCalc()
