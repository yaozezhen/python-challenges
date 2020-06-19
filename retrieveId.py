import urllib.request, json 
# function descriptor: retrieveId(usrname)
# grabs the id of a user if they exist in the list of members found at https://api.github.com/orgs/treehouses/members
# usrname - username of a potential member
# return type: string
# example: usrname - anikx7 => return "anikx7 has ID number: 26880012"
#          usrname - anikx8 => return "anikx8 does not exist in the group"
def retrieveId(usrname):
  url = urllib.request.urlopen("https://api.github.com/orgs/treehouses/members")
  data = json.loads(url.read())
  for item in data: 
    if (item["login"] == usrname): 
      return usrname + " has ID number: " + str(item["id"])
  return usrname + " does not exist in the group."

print(retrieveId("275vytran"))
