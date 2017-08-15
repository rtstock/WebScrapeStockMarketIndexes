# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 09:42:42 2015

@author: justin.malinchak
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 12:37:02 2015

@author: justin.malinchak
"""

#outputfile = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\Uploads\\Files Ready For Upload\\test8.csv'

# // Parameters
DataColumnTitle = 'DayTot'
localoutputfolder = 'C:\Batches\AutomationProjects\Investment Strategy\ETL\Uploads\Ready'
etluploadfolder = 'E:\\Batches\\development\\projects\\Investment Strategy\\ETL\\Uploads\\Ready'
downloadsfrombarclays = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\Downloads\\Unprocessed\\barclays'

import shutil
 
def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)

# //  Main processing

import datetime
filedatetime = datetime.datetime.today()
filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S%M')
outputfile = localoutputfolder + '\\barclays upload ' + filedatetime_string + '.csv'
uploadfile = etluploadfolder + '\\barclays upload ' + filedatetime_string + '.csv'

import os    
import csv
#downloadsfrombarclays = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\Downloads\\barclays\\'

mydict = {}

files = os.listdir(downloadsfrombarclays)
for filename in files:
    if filename[-5:] == '.muni':
        filepathname = os.path.join(downloadsfrombarclays, filename)
        
        '''
        # Read the file
        crs = open(filepathname, "r")
        f = open(filepathname, 'r')
        all_words = map(lambda l: l.split('\t'), f.readlines())
        for row in all_words:
            print row
        '''
        
        mycolumn = -1
        with open(filepathname, 'r') as f:
            reader = csv.reader(f, dialect='excel', delimiter='\t')
            for row in reader:
                for colid in range(len(row)):
                    if row[colid] == DataColumnTitle:
                        mycolumn = colid
                    elif mycolumn > 0 and colid == mycolumn:
                        #print row[1],row[mycolumn]
                        mydict[len(mydict)] = {'source':'BARCLAYS','measure':'Daily Returns','product1':'muni','id':row[0],'name':row[1],'period':row[2],'DataColumnTitle':DataColumnTitle,'datavalue':row[mycolumn]}
        # ==========================
        # print 'mycolumn=',mycolumn
        # ==========================
for k,v in mydict.items():
    print k,v

with open(outputfile, 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, mydict[0].keys(),delimiter = "|")
    w.writeheader()
    for k,v in mydict.items():
        w.writerow(v)

copyFile(outputfile, uploadfile)