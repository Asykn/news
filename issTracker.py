import urllib.request
import json
import webbrowser
from datetime import datetime

#people on iss
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("There are" + 
        str(result["number"]) + " astronauts on the ISS: \n\n")
people = result["people"]

for p in people:
    file.write(p['name'] + " - on board" + "\n")

#date and time
my_string = str(input('Enter date(yyyy-mm-dd hh:mm): '))
my_date = datetime.strptime(my_string, "%Y-%m-%d %H:%M")
print(my_date)

#open map
response = urllib.request.urlopen('http://api.open-notify.org/iss-now.json')
print(response)
obj = json.loads(response.read())
lat = obj['iss_position']['latitude']
long = obj['iss_position']['longitude']

url = 'https://www.openstreetmap.org/?mlat=' + str(lat) + '&mlon=' + str(long) + '#map=3/' + str(lat) + '/' + str(long)
webbrowser.open_new_tab(url)

