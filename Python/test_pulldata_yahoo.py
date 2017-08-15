# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:33:51 2015

@author: justin.malinchak
"""
#   DGS10   10-Year Treasury Constant Maturity Rate       1962-10-01
#   SP500   S&P 500 Daily                                 2005-05-18
#   DJIA    Dow Jones Industrial Average                  2005-05-18
#   VIXCLS  CBOE Volatility Index: VVIXCLS                1990-01-02  


import pulldata
import datetime
aapl = pulldata.Options('aapl', 'yahoo')
expiry = datetime.date(2015, 6, 19)
calls = aapl.get_call_data(expiry=expiry)
all_data = aapl.get_all_data()
#df = pulldata._get_hist_yahoo('SPY', '2014-01-01', '2015-12-31', 2, False)
print all_data(1)