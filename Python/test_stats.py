
#import pandas as pd
#import numpy as np
#df = pd.DataFrame({'A':[1,1,2,2],'B':[1,2,1,2],'values':np.arange(10,30,5)})
#
#print df
#df1 = df.groupby('A').agg(np.std, ddof=0)
#print df1
#
#df2 = df.groupby('A').agg(np.std, ddof=1)
#print df2

# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:33:51 2015

@author: justin.malinchak
"""
#   DGS10   10-Year Treasury Constant Maturity Rate       1962-10-01
#   SP500   S&P 500 Daily                                 2005-05-18
#   DJIA    Dow Jones Industrial Average                  2005-05-18
#   VIXCLS  CBOE Volatility Index: VVIXCLS                1990-01-02  
    
from datetime import datetime
import os

# ######################
# To load data from .pkl
import pandas
file_name = os.path.join('C:\\','Batches','MyPython','DataAgg','output','test.pkl')
df = pandas.read_pickle(file_name) 
print df.dtypes


#df.loc[df.value == '.', '.'] = 'NaN'
#print df
print df.dtypes

mydate = datetime.strptime('1990-02-21', '%Y-%m-%d')
print 'myvalue',mydate,df.at[mydate,'value']
#
##df2 = pandas.DataFrame(df.rows,1)
#for index, row in df.iterrows():
#    v = row['value'] #.strip()
#    #print index,v
#    if v == '.':
#        print index,v
#        df.remove(index)
#        
#        #mydict = {}        
#        #v_float = float(v)
#        #df2.loc[index] = float(v)
#
#        #mydict.update['date':index,'value':v_float]
#        #df2[df2.count] = v_float
#        #print index,v_float
#    #v_float = float(v)
#    #print'isdigit', index,v_float
#
##df['value'] = df['value'].astype(float)
##df.convert_objects(convert_numeric=True).dtypes
#
#print '-------------------------'
#print df.dtypes
##for k,v in d.items():
##    print(k,v)
#
#
#from scipy import stats
#from scipy.stats import norm
##print norm.__doc__
#
##r = norm.rvs(size=5)
##print r
#print 'mymean',df['value'].mean()