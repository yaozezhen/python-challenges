# function descriptor: countLetters2()
# counts the number of letters the user types when prompted
# return type: nothing
# example: Type a string consisting of whatever characters you want: 'fJi298 3_*4th'
#          There are 5 letters in fJi298 3_*4th
#          Would you like to type another string? [y|n] 'n'
#          Okay, bye :)
def countLetters2():
  while True: 
    string = input("Type a string consisting of whatever characters you want: ")
    count = 0
    for letter in string: 
      asc = ord(letter)
      if((asc > 64 and asc < 91) or (asc > 96 and asc < 123)): 
        count += 1
    print("There are " + str(count) + " letters in " + string)
    another = input("Woudl you like to type another string? [y|n] ")
    if(another == "n"): 
      print("Okay, bye :)")
      return

countLetters2()
