import random
# function descriptor: passwordGen(pl)
# randomly generates a strong password including numbers, letters, and special characters
# pl - password length (in characters), must be at least 12 and at most 16
# return type: string
# example: pl - 12 => return "f2inuPw9!8)*"

def passwordGen(): 
  while True: 
    pl = int(input("How long would you like your password to be? "))
    if (pl < 12 or pl > 16): 
      print("Password length must be at least 12 and at most 16.")
    else: 
      break
  check = 0
  repeat = 0
  while check < 4 or repeat == 1: 
    speChar = 0
    num = 0
    upper = 0
    lower = 0
    repeat = 0
    pwAscii = []
    for i in range(pl): 
      pwAscii.append(random.randint(33,126))
    for item in pwAscii:
      if ((item < 48) or (item > 57 and item < 65) or (item > 90 and item < 97) or (item > 122)): 
        speChar = 1
        break
    for item in pwAscii: 
      if (item > 47 and item < 58): 
        num = 1
        break
    for item in pwAscii: 
      if (item > 54 and item < 91): 
        upper = 1
        break
    for item in pwAscii: 
      if (item > 96 or item < 123): 
        lower = 1
        break
    check = speChar + num + upper + lower
    for i in range(pl-1): 
      for j in range(i+1,pl): 
        if (pwAscii[i] == pwAscii[j]): 
          repeat = 1
      if (repeat == 1): 
        break
  pw = []
  for item in pwAscii: 
    pw.append(chr(item))
  return "Your new password is: " + "".join(pw)

print(passwordGen())
