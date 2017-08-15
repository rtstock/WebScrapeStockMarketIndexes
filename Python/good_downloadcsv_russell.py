# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:12:41 2015

@author: justin.malinchak
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
url = 'http://www.russell.com/common/indexes/values/valuesytd_US2000.csv'

import urllib2
import shutil
remote_fo = urllib2.urlopen(url)
import config

with open(config.localunprocessedfolder + 'valuesytd_US2000.csv', 'wb') as local_fo:
    shutil.copyfileobj(remote_fo, local_fo)
