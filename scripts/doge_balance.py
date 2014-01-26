#!/usr/bin/env python
import requests

wallet = ""
r = requests.get("http://dogechain.info/chain/Dogecoin/q/addressbalance/"+wallet)

balance = float(r.text)

output = "{:,.2f}".format(balance)

print(output)
