# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:33:43 2015

@author: Justin.Malinchak
"""
import pandas
import os
import numpy
file_name = os.path.join('C:\\','Batches','MyPython','DataAgg','output','sp500.pkl')
df = pandas.read_pickle(file_name) 

# ################
# the value field was datatype string because there were records with '.'
# removed records with '.'
select = pandas.Series(['.'])
df = df[~df.value.isin(select)]

# ################
# This converts the field
df[['value']] = df[['value']].astype(float)

# ################
# check if the field converted to float
#print df.applymap(numpy.isreal)

df.convert_objects(convert_numeric=True).dtypes

df['STD'] = pandas.rolling_std(df['value'], 30, min_periods=30)
df['MAX'] = pandas.stats.api.expanding_max(df['value'])
print df
print '-------------------------'
#print df.dtypes

from scipy import stats
from scipy.stats import norm
print 'stats mean',stats.nanmean(df['value'],0)
print 'stats variation',stats.variation(df['value'],0)
print 'my std',df['value'].std(1)
print 'my mean',df['value'].mean()
print 'my var',df['value'].var()

#print 'my stdev',df['value'].stdev()


#select  = df.apply(lambda r : any([isinstance(e, basestring) for e in r ]),axis=1) 
#print df[~select]     