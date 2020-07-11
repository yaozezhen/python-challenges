# function descriptor: potatoCount(s)
# create a function to return the amount of potatoes there are in a string
# return type: integer
# example: s - "potatopotato" => return 2
#          s - "potatotomato" => return 1
def potatoCount(s):
  output = 0
  for i in range(len(s)-5): 
    if(s[i] == "p"): 
      if(s[i+1] == "o"): 
        if(s[i+2] == "t"): 
          if(s[i+3] == "a"): 
            if(s[i+4] == "t"): 
              if(s[i+5] == "o"): 
                output += 1
  return output

print(potatoCount("potatotomato"))
