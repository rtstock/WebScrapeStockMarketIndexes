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


# // Parameters
DataColumnTitle = 'MTD Total'   # can be [DayTot or MTDTot]
fileextension = '.agg'
localoutputfolder = 'C:\Batches\AutomationProjects\Investment Strategy\ETL\Uploads\Ready'
etluploadfolder = 'E:\\Batches\\development\\projects\\Investment Strategy\\ETL\\Uploads\\Ready'
downloadsfrombarclays = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\Downloads\\Unprocessed\\barclays'
#downloadsfrombarclays = 'C:\Batches\AutomationProjects\Investment Strategy\ETL\zTest'
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
outputfile = localoutputfolder + '\\barclays upload ' + fileextension[-3:] + ' ' + filedatetime_string + '.csv'
uploadfile = etluploadfolder + '\\barclays upload ' + fileextension[-3:] + ' ' + filedatetime_string + '.csv'

import os    
import csv
import re
#downloadsfrombarclays = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\Downloads\\barclays\\'

mydict = {}

files = os.listdir(downloadsfrombarclays)
for filename in files:
    if filename[-4:] == fileextension:
        filepathname = os.path.join(downloadsfrombarclays, filename)
        
        '''
        # Read the file
        crs = open(filepathname, "r")
        f = open(filepathname, 'r')
        all_words = map(lambda l: l.split('\t'), f.readlines())
        for row in all_words:
            print row
        '''
        checkingon = 0
        mycolumn = -1
        with open(filepathname, 'r') as f:
            reader = csv.reader(f, dialect='excel', delimiter='\t')
            for row in reader:
                #print len(row),row, 'xxxxxxxx'

                if 'MTD Total' in str(row):
                    print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                    mycharindex =  [ (i.start(), i.end()) for i in re.finditer('MTD Total', str(row))]
                    mycharindex_string = str(mycharindex[0])
                    mycharindex_string = mycharindex_string.replace('(','')
                    mycharindex_string = mycharindex_string.replace(')','')
                    mycharindex_string = mycharindex_string.replace(' ','')
                    mycharindex_start = int(mycharindex_string.split(',')[0])
                    mycharindex_end = int(mycharindex_string.split(',')[1])
                    #print mycharindex_start,mycharindex_end,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'
                    
                    checkingon = 1
                    
                if checkingon == 1:
                    mymtdreturn = str(row)[mycharindex_start:mycharindex_end]
                    onlydigits = mymtdreturn.replace(' ','').replace('.','').replace('-','')
                    
                    if not 'MTD Total' in str(row) and not onlydigits == 'Return' and onlydigits.isdigit() == False and len(onlydigits) > 0:
                        checkingon = 0
                        print 'zzzzzzzzzzzzzzzzzzzzzzzzz ' +  str(len(onlydigits)) + '/' + onlydigits + ' zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
                       
                    if len(str(row)) > mycharindex_end or 'MTD Total' in str(row) :
                        #print str(row)[2:21],str(row)[22:31],str(row)[32:38],mymtdreturn,filename,'|||||',row[0], 'xxxxxxxx', str(row)[32:39]
                        issuename = str(row)[2:23]
                        if not issuename[:2] == '  ':
                            if mymtdreturn.strip().replace('-','').replace('.','').isdigit() == True:
                                mydict[len(mydict)] = {'source':'barclays','category':'agg','issue':issuename.strip(),'numofissues':str(row)[23:31].strip(),'pricereturn':str(row)[32:38].strip(),'mtdtotalreturn':mymtdreturn.strip(),'filename':filename}
                        
                #print len(str(row))
                #if len(row) > 0:
                #    print 'issue:',str(row)[2:21],'NumberIssues:',str(row)[22:31], str(row)[32:39], str(row)[77:88],'|||||',row[0], 'xxxxxxxx', str(row)[32:39]
                    
#                for colid in range(len(row)):
#                    if row[colid] == DataColumnTitle:
#                        mycolumn = colid
#                    elif mycolumn > 0 and colid == mycolumn:
#                        #print row[1],row[mycolumn]
#                        mydict[len(mydict)] = {'source':'BARCLAYS','measure':DataColumnTitle,'product':fileextension,'id':row[0],'name':row[1],'period':row[2],'datavalue':row[mycolumn],'filename':filename}
        
        # ['U.S. Aggregate           9420    5.92     5.64   3.23   7.92  104.46    2.36  17739851    100.00    100.00\n']
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
#        
# =============================
# when you're ready to upload file, enable this...
#
# copyFile(outputfile, uploadfile)
#
# =============================