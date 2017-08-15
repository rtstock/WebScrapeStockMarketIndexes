# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 12:37:02 2015

@author: justin.malinchak

Notes:
    Reads all files in folder [downloadsfromnareit] and creates a pipe (|) delimited csv file for bulk loading to sqlserver
    2nd parsed string in file name should be one of these: ['MonthlyYTDReturns', 'MonthlyHistoricalReturns']
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

# Parameters
localoutputfolder = 'C:\Batches\AutomationProjects\Investment Strategy\ETL\Uploads\Ready'
etluploadfolder = 'E:\\Batches\\development\\projects\\Investment Strategy\\ETL\\Uploads\\Ready'
downloadsfromnareit = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\Downloads\\Unprocessed\\nareit'
datasection = 'Equity REITs'

import datetime
filedatetime = datetime.datetime.today()
filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S%M')
outputfile = localoutputfolder + '\\nareit upload ' + filedatetime_string + '.csv'
uploadfile = etluploadfolder + '\\nareit upload ' + filedatetime_string + '.csv'

import xlrd
from xlrd import open_workbook
import os    
#downloadsfromnareit = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\Downloads\\nareit\\'


files = os.listdir(downloadsfromnareit)
mydict = {}
smalldict = {}
for filename in files:
    #print filename
    fullpath = os.path.join(downloadsfromnareit, filename)
    lsfilename = filename.split(' ')
    
    nameofdata = lsfilename[0]
    categoryofdata = lsfilename[1]
    dateofdata = lsfilename[2].replace('.xls','')
    if categoryofdata in ['MonthlyYTDReturns', 'MonthlyHistoricalReturns']:
        print 'sourcefile:',fullpath
        wb = open_workbook(fullpath)
        values = []
        for s in wb.sheets():
            #print 'Sheet:',s.name
            headerrow = -1
            headercol = -1
            datavaluecolumn = -1
            details = ''
            #print 'datavaluecolumn set to zero'
            for row in range(1, s.nrows):  
                rowcontents = s.row(row)
                #print rowcontents
                #myset = set(rowcontents)
                #print myset
                #if 'Equity REITs' in myset:
                  # do stuff
                #    print rowcontents.index('All Equity REITs'),rowcontents
    #            col_names = s.row(row)
    #            col_value = []
                for name, col in zip(rowcontents, range(s.ncols)):
                    value  = (s.cell(row,col).value)
                    if value == datasection:
                        #print value,'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',col
                        datavaluecolumn = col
                        print 'datavaluecolumn set to',col
                        break
                if datavaluecolumn > 0:
                    date_string  = str((s.cell(row,0).value)).strip()
                    value_string  = str((s.cell(row,datavaluecolumn).value)).strip()
                    if value_string.replace('.','').replace('-','').isdigit() == False and len(value_string) > 0:
                        #print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                        #print value_string
                        details = details + value_string + '-'
                    if date_string.replace('.','').isdigit() and len(date_string) > 0:
                        date_asfloat = float(date_string)
    #                    import xlrd
    #                    import datetime
                        date_astuple = xlrd.xldate_as_tuple(date_asfloat, 0)
                        date_asdate = datetime.date(date_astuple[0],date_astuple[1],date_astuple[2])
                        date_asdate_string = str(date_asdate)
                        
                        #print date_string, value_string,'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',col
                        if date_string != '':
                            if value_string != '':
                                #print date_asdate,value_string,filename
                                smalldict = {'details':details[:len(details)-1],'datasection':datasection,'date_asdate_string':date_asdate_string,'value_string':value_string,'filename':filename}
                                mydict[len(mydict)] = smalldict
                                    
    #                if value == 'nareit Index':
    #                    headerrow = row
    #                    headercol = col
    #                if headerrow > 0:
    #                    rowheadertext = (s.cell(row,headercol).value)
    #                    colheadertext = (s.cell(headerrow,col).value)
    #                    if len(rowheadertext) == 0:
    #                        headerrow = -1
    #                
    #                    if headerrow > 0 and row > headerrow and col > headercol and len(colheadertext) > 0:
    #                        productname = rowheadertext
    #                        periodtext = colheadertext
    #                        datavalue = s.cell(row,col).value
    #                        #print nameofdata,dateofdata,categoryofdata,productname,periodtext,datavalue 
    #                        smalldict = {'nameofdata':nameofdata,'dateofdata':dateofdata,'categoryofdata':categoryofdata,'productname':productname,'periodtext':periodtext,'datavalue':datavalue,'filename':filename}
    #                        mydict[len(mydict)] = smalldict

for k,v in mydict.items():
    print k,v

import csv
with open(outputfile, 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, mydict[0].keys(),delimiter = "|")
    w.writeheader()
    for k,v in mydict.items():
        w.writerow(v)

print 'your file for sql is here:',outputfile
#
#copyFile(outputfile, uploadfile)
#
#

#
#import csv
#keys = mydict[0].keys()
#print keys
#with open('C:\\Batches\\AutomationProjects\\Investment Strategy\\Uploads\\Files Ready For Upload\\test.csv', 'wb') as output_file:
#    dict_writer = csv.DictWriter(output_file, keys)
#    dict_writer.writeheader()
#    dict_writer.writerows(mydict)