# function descriptor: countLetters(word)
# keeps asking the user to count the letters in the word until they get it correct
# word - any word that you want to user to count the number of letters in
# return type: nothing; program should end when the user types the correct amount of letters
# example: How many letters are in the word apple? '6'
#          Nope, try again! How many letters are in the word apple? '5'
#          Nice job! You got it :)
def countLetters(word):
  a = len(word)
  while True: 
    q = input("How many letters are in the word " + word + "? ")
    if (int(q) == a): 
      break
    print("Nope, try again! ")
  print("Nice job! You got it!")
  return 

countLetters("apple")
