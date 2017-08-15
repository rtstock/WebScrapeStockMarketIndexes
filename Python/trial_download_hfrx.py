# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:12:41 2015

@author: justin.malinchak

Notes:
    Run this once per month to get the latest data from HFRX.
    Gets a file in Excel format
"""
import sys
print (sys.version)


#url = 'https://www.hedgefundresearch.com/sites/default/files/index_data/hfrx_index_data.csv'
url = 'https://www.hedgefundresearch.com/sites/default/files/index_data/hfrx_daily_index_data.csv'
myindex = 'HFRXGI-D'

import config
outputpath =  config.localunprocessedfolder + '\\hfrx'

import datetime
filedatetime = datetime.datetime.today()
filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S%M')

print filedatetime_string
outputfile = outputpath + '\\hfrx monthly ' + filedatetime_string + '.csv'

print 'pulling hfrx...'
import requests
import shutil
user = 'justin.malinchak@ipcanswers.com'
password = 'Flicker01'
r = requests.get(url, auth=(user, password))
print r.status_code
print r.headers['content-type']
print r.encoding
#print r.text:

import csv
import requests
import datetime
d0 = datetime.datetime.today()

f_values = []
with requests.Session() as s:
    download = s.get(url)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        
        if len(row) > 3:
            
            if row[2] == 'HFRXEH':
                s_date = row[0]
                d1 = datetime.datetime.strptime(s_date,"%m/%d/%Y")
                delta = d0 - d1
                if delta.days > 30:
                    break
                s_pct = row[3]
                f0_pct = s_pct.replace('%', '')
                f0_date = d1.strftime('%Y%m%d')
                f_values.append([f0_date, f0_pct])
print f_values

f_final = []
f_final.append('Record Type,Index Code,To Date')
for item in f_values:
    f_final.append('MID,'+myindex+','+item[0])

f_final.append('Record Type,Index Code,From Date,To Date,,,,,,,,')
for item in f_values:
    f_final.append('MIH,'+myindex+','+item[0]+','+item[0]+',,,,,,,,')
f_final.append('Record Type,Index Code,Index Node Code,From Date,To Date,,,,,Weight,Return,Local Return ')
for item in f_values:
    f_final.append('MIV,'+myindex+','+myindex+','+item[0]+','+item[0]+',,,,,1,'+item[1]+','+item[1])
f_final.append(',,,,,,,,,,,')
for item in f_final:
    print item


#import csv

filepath = 'P:\\Apl\\APL Benchmarks\\Data\\$Daily\\automated\\'+myindex+' '+ d0.strftime('%Y-%m-%d %H.%M.%S') + '.csv'

with open(filepath,'wb') as resultFile:
    wr = csv.writer(resultFile, quoting=csv.QUOTE_NONE, escapechar="\"", quotechar="\\")
    for row in f_final:
        s1 = str(row).replace('"','')
        wr.writerow(s1)
    


