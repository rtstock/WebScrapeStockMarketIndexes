# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 12:37:02 2015

@author: justin.malinchak

Notes:
    Reads all files in folder [localunprocessedfolder] and creates a pipe (|) delimited csv file for bulk loading to sqlserver
    The completed file for uploading is saved to [localoutputfile], then that file is copied to the sql server file system folder [etluploadfolder]
"""

#outputfile = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\Uploads\\Files Ready For Upload\\test8.csv'

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

############
# Parameters

import config
config.localunprocessedfolder 
config.localprocessedfolder 
config.localuploadsreadyfolder 
config.serveruploadsreadyfolder 

#localunprocessedfolder = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\\Downloads\\Unprocessed\\barclays'
localunprocessedfolder = config.localunprocessedfolder +'\\msci'
localprocessedfolder = config.localprocessedfolder+'\\msci'
localoutputfolder = config.localuploadsreadyfolder  #'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\\Uploads\\Ready'
etluploadfolder = config.serveruploadsreadyfolder  #'E:\\Batches\\development\\projects\\Investment Strategy\\ETL\\Uploads\\Ready'


import datetime
filedatetime = datetime.datetime.today()
filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S%M')
outputfile = localoutputfolder + '\\msci upload returnsdaily ' + filedatetime_string + '.csv'
uploadfile = etluploadfolder + '\\msci upload returnsdaily ' + filedatetime_string + '.csv'

from xlrd import open_workbook
import os    
#localunprocessedfolder = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\Downloads\\msci\\'


files = os.listdir(localunprocessedfolder)
mydict = {}
smalldict = {}
for filename in files:
    localunprocessedcsvpathname = os.path.join(localunprocessedfolder, filename)
    lsfilename = filename.split(' ')
    nameofdata = lsfilename[0]
    dateofdata = lsfilename[1]
    categoryofdata = lsfilename[2].replace('.xls','')
    print localunprocessedcsvpathname
    wb = open_workbook(localunprocessedcsvpathname)
    values = []
    for s in wb.sheets():
        #print 'Sheet:',s.name
        headerrow = -1
        headercol = -1
        for row in range(1, s.nrows):        
            col_names = s.row(row)
            col_value = []
            for name, col in zip(col_names, range(s.ncols)):
                value  = (s.cell(row,col).value)
                if value == 'MSCI Index':
                    headerrow = row
                    headercol = col
                if headerrow > 0:
                    rowheadertext = (s.cell(row,headercol).value)
                    colheadertext = (s.cell(headerrow,col).value)
                    if len(rowheadertext) == 0:
                        headerrow = -1
                
                    if headerrow > 0 and row > headerrow and col > headercol and len(colheadertext) > 0:
                        productname = rowheadertext
                        periodtext = colheadertext
                        datavalue = s.cell(row,col).value
                        #print nameofdata,dateofdata,categoryofdata,productname,periodtext,datavalue 
                        smalldict = {'nameofdata':nameofdata,'dateofdata':dateofdata,'categoryofdata':categoryofdata,'productname':productname,'periodtext':periodtext,'datavalue':datavalue,'filename':filename}
                        mydict[len(mydict)] = smalldict

mydictdaily = {}
for k,v in mydict.items():
    if v['periodtext'] == 'Day':
        if v['productname'] == 'EAFE':
            if v['categoryofdata'] == 'DM_Gross':
                mydictdaily[len(mydictdaily)] = v

for k,v in mydict.items():
    if v['periodtext'] == 'Day':
        if v['productname'] == 'ACWI':
            if v['categoryofdata'] == 'AC_Gross':
                mydictdaily[len(mydictdaily)] = v
##    # ###############################################################################
##    # Move unprocessed file to processed folder after all 3 datacolumntitles complete
##    # 
##    localprocessedcsvpathname = os.path.join(localprocessedfolder,filename) #'E:\Batches\development\projects\Investment Strategy\ETL\Uploads\Ready'.encode('string_escape')
##    if os.path.exists(localprocessedcsvpathname):
##        os.remove(localprocessedcsvpathname)
##    shutil.move(localunprocessedcsvpathname, localprocessedfolder)
##    # #####################


##    # ###############################################################################

import csv

if len(mydictdaily) == 0:
    print('No records to process, possibly no msci files found.')
else:
    with open(outputfile, 'wb') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, mydictdaily[0].keys(),delimiter = "|")
        w.writeheader()
        for k,v in mydictdaily.items():
            w.writerow(v)
    
    copyFile(outputfile, uploadfile)
    print 'you can find you file here:',uploadfile

    #print 'you can find you file here:',outputfile
    print 'process completed'
##    # ###############################################################################
