import urllib.request, json 
# function descriptor: time(zone,format)
# finds the current time in requested region and format, see http://worldclockapi.com/api/json/est/now
# zone - EST or PST, represents time zone (East coast, West coast)
# format - 12 or 24, represents 12-hour clock or 24-hour clock
# return type: string
# example: (zone,format) - ("EST", 12) => return "It is currently 2:25 on the East coast"
#          (zone,format) - ("EST", 24) => return "It is currently 14:25 on the East coast"
def time(zone,frmat):
  url = urllib.request.urlopen("http://worldclockapi.com/api/json/est/now")
  data = json.loads(url.read())
  time = data["currentDateTime"]
  timeLs = []
  hrLs = []
  minLs = []
  for letter in time: 
    timeLs.append(letter)
  for i in range(11): 
    timeLs.pop(0)
  for i in range(6): 
    timeLs.pop(5)
  for i in range(3,5): 
    minLs.append(timeLs[i])
  minute = ":" + "".join(minLs)
  if(timeLs[0] == "0"): 
    timeLs.pop(0)
    hrLs.append(timeLs[0])
  else: 
    for i in range(2): 
      hrLs.append(timeLs[i])
  hour = "".join(hrLs)
  if(zone == "EST"): 
    if(frmat == 12): 
      if(int(hour) > 11): 
        hour = str(int(hour)-12)
        return "It is currently " + hour + minute + " PM on the East coast. "
      else: 
        return "It is currently " + hour + minute + " AM on the East coast. "
    if(frmat == 24): 
      return "It is currently " + hour + minute + " on the East coast. "
  if(zone == "PST"): 
    hour = str((int(hour)-3)%24)
    if(frmat == 12): 
      if(int(hour) > 11): 
        hour = str(int(hour)-12)
        return "It is currently " + hour + minute + " PM on the West coast. "
      else: 
        return "It is currently " + hour + minute + " AM on the West coast. "
    if(frmat == 24): 
      return "It is currently " + hour + minute + " on the West coast. "
print(time("PST",12))
