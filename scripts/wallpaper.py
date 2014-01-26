#!/usr/bin/env python

import glob
import random
import os

wallpaper_dir = ""
files = glob.glob(wallpaper_dir+"*.jpg")
random.shuffle(files)
command = "feh --no-fehbg --bg-fill " + files[0] + " " + files[1]
#print(command)
os.system(command)

