#coding:utf-8
"""
------------------------------------------------
@File Name    : enginerring_01_two_quantiative_variables
@Function     : 
@Author       : Minux
@Date         : 2018/9/17
@Revised Date : 2018/9/17
------------------------------------------------
"""
import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt
import re
import mailbox
import csv

gapminder = pd.read_csv('gapminder.csv')
# print(gapminder.info())
italy = gapminder.query('country == "Italy"')
# italy.plot.scatter('year','population')

# gapminder.query('country == "India"').plot.scatter('year','population',label='India')

# italy.plot.scatter('year','gdp_per_day',logy=True)

# italy.plot.scatter('gdp_per_day','life_expectancy',logx=True)

size = np.where(italy.year%10==0,32,2)
data = gapminder.query('(country == "Italy") or (country == "United States")')
color = np.where(data.country == 'Italy','blue','orange')
data.plot.scatter('gdp_per_day','life_expectancy',logx=True,c=color,s=size)

plt.legend()
plt.show()