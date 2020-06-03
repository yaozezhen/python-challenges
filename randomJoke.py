import urllib.request, json 
# function descriptor: randomJoke()
# generates a random joke using the given URL containing a JSON object
# your task is to figure out how JSON objects work since the joke is inside of it already, a hint is given below ;)
# return type: string
def randomJoke():
  url = urllib.request.urlopen("https://api.icndb.com/jokes/random/")
  data = json.loads(url.read())
  # uncomment the line immediately below to see the contents of data, JSON objects are similar to dictionaries
  # print (data)
  # fill-in code
