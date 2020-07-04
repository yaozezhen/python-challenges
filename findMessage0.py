# function descriptor: findMessage0()
# objective: find the hidden message in message0.txt
# return type: string
f = open("message0.txt","r")
for line in f: 
  for i in range(len(line)): 
    if(ord(line[i]) > 96 and ord(line[i]) < 123): 
      print(line[i])
