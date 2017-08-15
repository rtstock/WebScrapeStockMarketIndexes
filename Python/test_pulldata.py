# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:33:51 2015

@author: justin.malinchak
"""
#   DGS10   10-Year Treasury Constant Maturity Rate       1962-10-01
#   SP500   S&P 500 Daily                                 2005-05-18
#   DJIA    Dow Jones Industrial Average                  2005-05-18
#   VIXCLS  CBOE Volatility Index: VVIXCLS                1990-01-02  

fred_datasetname = 'VIXCLS'
start_datestring = '1990-01-02'
pickel_filename = fred_datasetname + '.pkl'

from datetime import datetime

startdate = datetime.strptime(start_datestring, '%Y-%m-%d')
#fred_datasetname = fred_datasetname.capitalize()
#==============
print startdate
#==============

import pulldata
df = pulldata.DataReader(fred_datasetname, "fred") #,start=startdate
print df
df['new_col'] = range(1, len(df) + 1)

#d = {}
#for t in df.itertuples():
#    d[t[0]] = t
    
import os
# ###############
# to save as .csv
#file_name = os.path.join('C:\\','Batches','MyPython','DataAgg','output','test.csv')
#df.to_csv(file_name)

# ######################
# To save data as a .pkl
file_name = os.path.join('C:\\','Batches','MyPython','DataAgg','output',pickel_filename)
df.to_pickle(file_name) 

# ######################
# To load data from .pkl
import pandas
file_name = os.path.join('C:\\','Batches','MyPython','DataAgg','output',pickel_filename)
df = pandas.read_pickle(file_name) 
print df
#for k,v in d.items():
#    print(k,v)

#mydate = datetime.strptime('2007-12-03', '%Y-%m-%d')
#print 'mydate',mydate,df.at[mydate,'value']


#df.to_csv(file_name, sep=',')
#o = pulldata.DataReader.get_data_fred('10-Year Treasury Constant Maturity Rate')

#df.loc[df.value == '.', '.'] = 'NaN'
#print df
print df.dtypes
print list(df.columns.values)
mydate = datetime.strptime('2015-05-22', '%Y-%m-%d')
print 'myvalue',mydate,df.at[mydate,'VIXCLS']