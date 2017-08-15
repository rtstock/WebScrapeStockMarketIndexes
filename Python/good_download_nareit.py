# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:12:41 2015

@author: justin.malinchak

Notes:
    Run this once per month to get the latest data from NAREIT.
    Gets a file in Excel format
"""
import sys
print (sys.version)

#import urllib2
#import csv
##url = 'https://docs.google.com/spreadsheet/pub?key=0AmNIZgbwy5TmdENjMmZ2cm5VQXJJMWlQVENIek5Ta2c&amp;output=csv'
#url = 'http://www.russell.com/common/indexes/values/valuesytd_US2000.csv'
#data = urllib2.urlopen(url)
##data = data.splitlines()
#reader = csv.DictReader(data)
#for record in reader:
#   print record


url = 'https://www.reit.com/sites/default/files/returns/MonthlyReturns.xls'

import config
outputpath =  config.localunprocessedfolder + '\\nareit'

import datetime
filedatetime = datetime.datetime.today()
filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S%M')

print filedatetime_string
outputfile = outputpath + '\\nareit MonthlyYTDReturns ' + filedatetime_string + '.xls'

print 'pulling nareit...'
import urllib2
import shutil
remote_fo = urllib2.urlopen(url)

with open(outputfile,'wb') as local_fo:
    shutil.copyfileobj(remote_fo, local_fo)

print 'You can find your file here:'
print outputfile