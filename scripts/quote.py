#!/usr/bin/env python

import requests
import random

mashape_key = ""
endpoints = ["qt","got","bb"]
random.shuffle(endpoints)
ep = endpoints[0]
url = "https://community-random-movie-quotes.p.mashape.com/"+ep 
headers = {"X-Mashape-Authorization": mashape_key}

r =  requests.get(url, headers=headers)
full_quote = r.text.split("\n")[0]
parts = full_quote.split(":")

formatted = "\\\"" + parts[1].strip() + "\\\" --" + parts[0] 

print (formatted)

