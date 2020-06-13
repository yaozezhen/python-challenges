import urllib.request, json 
# function descriptor: randomEO()
# determines if the list of 10 random numbers returned from the URL are odd or even using JSON 
# website URL: https://www.passwordrandom.com/query?command=int&min=0&max=10000&format=json&count=10 
# return type: list of 'odd' and 'even' strings
# example: return ['odd','even','odd','even','even','odd','odd','even','odd','even']
def randomEO():
  url = urllib.request.urlopen("https://www.passwordrandom.com/query?command=int&min=0&max=10000&format=json&count=10")
  data = json.loads(url.read())
  ls = data["random"]
  output = []
  for i in range(10): 
    if (ls[i] % 2 == 0): 
      output.append("even")
    else: 
      output.append("odd")
  return output
