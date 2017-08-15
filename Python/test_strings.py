# -*- coding: utf-8 -*-
"""
Created on Wed May 20 13:28:03 2015

@author: Justin.Malinchak
"""

fred_datasetname = 'VIXCLS'
start_datestring = '1990-01-02'
pickel_filename = fred_datasetname + '.pkl'

from datetime import datetime

startdate = datetime.strptime(start_datestring, '%Y-%m-%d')
print startdate