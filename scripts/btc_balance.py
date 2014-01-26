#!/usr/bin/env python
import requests
import json

wallet = ""

r = requests.get("http://blockchain.info/address/"+wallet+"?format=json")

j = json.loads(r.text)

output = "{:,.8f}".format(j["final_balance"]/100000000)

print(output)
