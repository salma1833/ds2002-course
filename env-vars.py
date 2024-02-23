#!/usr/bin/python3

import os

os.environ["FAV_SPORT"] = "Basketball"
os.environ["MAJOR"] = "Commerce"
os.environ["COLOR_SHIRT"] = "Blue"

FAV_SPORT = input('What is your favorite sport? ')
os.environ["FAV_SPORT"] = FAV_SPORT

MAJOR = input('What is your major? ')
os.environ["MAJOR"] = MAJOR

COLOR_SHIRT = input('What color shirt are you wearing? ')
os.environ["COLOR_SHIRT"] = COLOR_SHIRT

print("Favorite Sport:", os.getenv("FAV_SPORT"))
print("Major:", os.getenv("MAJOR"))
print("Current Shirt Color:", os.getenv("COLOR_SHIRT"))
