#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 23:55:25 2019

@author: yyn
"""

import pandas as pd
cf = pd.read_csv("nyc_restaurant.csv")

#change from string to date
import datetime
cf['INSPECTION DATE'] = pd.to_datetime(cf['INSPECTION DATE'])

#get the month of all the inspection date
cf['INSPECTION MONTH'] = cf['INSPECTION DATE'].dt.month

#clean the 1/1/1900
cf1 = cf[cf['INSPECTION DATE'] > datetime.datetime(2000, 1, 1)]

#count the number of all the grades by month
mg = cf1.groupby(['INSPECTION MONTH', 'GRADE'])['CAMIS'].count().unstack()

mg['TOTAL'] = mg.sum(axis = 1)

import matplotlib.pyplot as plt

#get the percentage of grade A
(mg['A'] / mg['TOTAL']).plot.bar()
plt.title("Grade A distribution by month")
plt.show()

