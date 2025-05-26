# Demonstrates iterating over JSON

import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit() # sys.exit breaks the entire program but break breaks the loop VVIMPORTANT

response = requests.get(
    "https://itunes.apple.com/search?entity=song&term=" + sys.argv[1] # Here in the link there is no limit
)
o = response.json()
for result in o["results"]:
    print(result["trackName"])
