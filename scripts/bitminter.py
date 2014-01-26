#!/usr/bin/env python

import requests
import json

key = ""
username = ""

r = requests.get("http://bitminter.com/api/users/"+username+"?key="+key)
data = json.loads(r.text)
output = data["hash_rate"] + " MH/s (" + str(data["balances"]["BTC"]) + ")"
print(output)  