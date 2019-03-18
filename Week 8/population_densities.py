#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 10:20:43 2019

@author: anirudhkulkarni
"""

import pandas as pd
from area import area
import json
from pprint import pprint


with open('ca_pop.json') as f:
    data = json.load(f)

pprint(data["features"][0])


for i in range(0,len(data["features"])):
    population = data["features"][i]["properties"]["POP10"]
    square_area = area(data["features"][i]["geometry"]) * 0.000000386102158542
    pop_density = population/square_area
    data["features"][i]["properties"]["pop_density"] = pop_density

with open('ca_pop_density.json', 'w') as outfile:  
    json.dump(data, outfile)