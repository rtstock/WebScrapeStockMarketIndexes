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
min_date = d0

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
                if d1 < min_date:
                    min_date = d1
                    f0_date_min = f0_date
                f_values.append([f0_date, f0_pct])
print f_values


#import csv

filepath = 'P:\\Apl\\APL Benchmarks\\Data\\$Daily\\automated\\'+myindex+' '+ d0.strftime('%Y-%m-%d %H.%M.%S') + '.csv'

#with open(filepath,'wb') as resultFile:
#    wr = csv.writer(resultFile, quoting=csv.QUOTE_NONE, escapechar="\"", quotechar="\\")
#    for row in f_final:
#        #s1 = str(row).replace('"','')
#        wr.writerow([row])

if len(f_values) > 0:
    f_final_1 = []
    f_final_1.append(['Record Type','Index Code','To Date'])
    f_final_1.append(['MID',myindex,f0_date_min])
    #for item in f_values:
    #    f_final_1.append(['MID',myindex,item[0]])

    f_final_2 = []
    f_final_2.append(['Record Type','Index Code','From Date','To Date','','','','','','','',''])
    for item in f_values:
        f_final_2.append(['MIH',myindex,item[0],item[0],'','','','','','','',''])

    f_final_3 = []    
    f_final_3.append(['Record Type','Index Code','Index Node Code','From Date','To Date','','','','','Weight','Return','Local Return'])
    for item in f_values:
        f_final_3.append(['MIV',myindex,myindex,item[0],item[0],'','','','','1',item[1],item[1]])
    f_final_3.append(['','','','','','','','','','','',''])
    
    for item in f_final_1:
        print item
    for item in f_final_2:
        print item
    for item in f_final_3:
        print item          

    
    import pandas as pd
                
    headers = f_final_1.pop(0)
    df_final_1 = pd.DataFrame(f_final_1,columns=headers)
    
    headers = f_final_2.pop(0)
    df_final_2 = pd.DataFrame(f_final_2,columns=headers)

    headers = f_final_3.pop(0)
    df_final_3 = pd.DataFrame(f_final_3,columns=headers)


    '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                    output to CSV
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
    import os
    #filelocation_string = resolved_destination_pathfile #myoutputfolder + "\\intraday " + today_datestring + ' ' + symbol +'.csv'
    filelocation_string = 'P:\\Apl\\APL Benchmarks\\Data\\$Daily\\automated\\'+myindex+' '+ d0.strftime('%Y-%m-%d %H.%M.%S') + '.csv'
    if os.path.isfile(filelocation_string) == True:
        os.remove(filelocation_string)
    if os.path.isfile(filelocation_string) == True:
        print 'Could not delete file',filelocation_string
    else:
        print 'Attempting to create filelocation_string',filelocation_string
        with open(filelocation_string, 'w') as f:
            df_final_1.to_csv(f, header=True,index=False)
        with open(filelocation_string, 'a') as f:
            df_final_2.to_csv(f, header=True,index=False)
        with open(filelocation_string, 'a') as f:
            df_final_3.to_csv(f, header=True,index=False)

    print 'You can find your file here',filelocation_string   


