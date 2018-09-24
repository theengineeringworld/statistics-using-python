#coding:utf-8
"""
------------------------------------------------
@File Name    : enginerring_02_graph_visualization
@Function     : 
@Author       : Minux
@Date         : 2018/9/24
@Revised Date : 2018/9/24
------------------------------------------------
"""
import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import style
style.use('ggplot')
import pandas.plotting

from IPython import display
from ipywidgets import interact,widgets

import re
import mailbox
import csv


gap_minder = pd.read_csv('gapminder.csv')

def plot_year(year,info_tag=False):
    data = gap_minder[gap_minder.year==year].sort_values('population', ascending=False)

    if info_tag:
        population_info()

    color = data.age5_surviving
    area = 3e-6*data.population

    # customize edge color
    edgecolor = data.region.map({'Africa':'skyblue','Europe':'gold','America':'palegreen','Asia':'coral'})

    # plt.cla()
    data.plot.scatter('gdp_per_day','life_expectancy',logx=True,s=area,c=color,
                      colormap=matplotlib.cm.get_cmap('Purples_r'),vmin=55,vmax=100,linewidths=1,edgecolors=edgecolor,
                      sharex=False, figsize=(10,7))

    for level in [4, 16, 64]:
        plt.axvline(level, linestyle=':', color='k')

    plt.axis(xmin=1, xmax=500, ymin=30, ymax=100)
    plt.title('GDP-LIFE-EXPECTANCY_{}'.format(year))
    plt.xlabel('$gdp-per-day$')
    plt.ylabel('$life-expectancy$')


def population_info():
    res = gap_minder[gap_minder.year==2015].groupby('region').population.sum()
    print(res)

def dynamic_plotting_func():
    # interact(plot_year, year=range(1960,1970))
    # population_info()
    year_list = [1965, 1966, 1967]
    plt.ion()
    for _year in year_list:
        plot_year(_year)
        plt.pause(2)
        if _year != year_list[-1]:
            plt.close()
    plt.ioff()
    plt.show()

def plot_matrix_func():
    gap_minder.set_index('year',inplace=True)
    gap_minder['log10_gdp_per_day'] = np.log10(gap_minder['gdp_per_day'])
    data = gap_minder.loc[2015,['log10_gdp_per_day','life_expectancy','age5_surviving','babies_per_woman']]
    pandas.plotting.scatter_matrix(data, figsize=(9,9))
    plt.show()

if __name__ == '__main__':
    plot_matrix_func()


















