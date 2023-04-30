import pytz  #pip install pytz
import math
import csv
from geopy.distance import distance  #pip install geopy
from datetime import datetime
from fit_file import read

# Skriv en funktion som omregner fra tempo (min/km) til hastighed (m/s) 
# - (Write a function that converts from pace (min/km) to speed (m/s))
tempoToSpeed = lambda tempo: 1000 / (tempo * 60)

