#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 21:35:00 2020

@author: Angel
"""

import requests
import pandas as pd


resp = requests.get("https://api.covidtracking.com/v1/us/daily.json")
data = resp.json()

# loaded data into dateframe
df = pd.DataFrame.from_dict(data)
