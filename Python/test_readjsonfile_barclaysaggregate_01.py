# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:12:41 2015

@author: justin.malinchak

Notes:
    Run this once per month to get the latest data from HFRX.
    Gets a file in Excel format
"""


#################################################################################
myindex = 'SHLAGG-D'
numberofdaysback = -3000
#################################################################################

import config

import datetime
import os

import json

d0 = datetime.datetime.today()
today = datetime.date.today()
earliest_date = today
print 'today is:', today
dict_of_date8s = {}
iref = numberofdaysback
while True:
    if iref > 0:
        break
    refdate = today + datetime.timedelta(days=iref)
    if refdate < earliest_date:
        earliest_date = refdate
    refdate8 = str(refdate).replace('-','')
    dict_of_date8s[len(dict_of_date8s)] = refdate8
    iref = iref + 1

earliest_date8 = str(earliest_date).replace('-','')
print earliest_date8
print '----------------------------------------------'

savedjsonfile = os.path.join(config.localdatafileoutputpath,'dailyreturns-barclays-usaggregate.json')

# open savedjsonfile into testing_dict, and print key values to screen
with open(savedjsonfile) as f:
    returns_dict = json.load(f)
print 'ok...'
if len(returns_dict) > 0:
    for key, value in sorted(dict_of_date8s.iteritems()):
        #print value
        if value in returns_dict:
            this_dict = returns_dict[value]
            print this_dict['prevdate'],this_dict['currdate'],this_dict['prevmv'],this_dict['currmv']
            
