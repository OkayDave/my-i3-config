#!/usr/bin/env python

import requests
import json
import inflection

lng="0.0"
lat="0.0"
mashape_key=""

url = "https://metwit-weather.p.mashape.com/weather/?location_lat=%(lati)s&location_lng=%(long)s" % {"long": lng, "lati": lat}
r = requests.get(url, headers={
    "X-Mashape-Authorization": mashape_key
  }
);

data = json.loads(r.text)
now = data["objects"][0]["weather"]

weather = now["status"] + " " + str(int(now["measured"]["temperature"]-273))
print(weather)
