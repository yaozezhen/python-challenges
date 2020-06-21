import urllib.request, json 
# function descriptor: time(zone,format)
# finds the current time in requested region and format, see http://worldclockapi.com/api/json/est/now
# zone - EST or PST, represents time zone (East coast, West coast)
# format - 12 or 24, represents 12-hour clock or 24-hour clock
# return type: string
# example: (zone,format) - ("EST", 12) => return "It is currently 2:25 on the East coast"
#          (zone,format) - ("EST", 24) => return "It is currently 14:25 on the East coast"
def time(zone,format):
  # fill-in code here
