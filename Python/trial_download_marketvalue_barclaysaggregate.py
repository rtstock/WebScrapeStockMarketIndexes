'''
# Notes
    Downloads last 5 days of Barclays data from lehman via ftp
'''
from ftplib import FTP
import os, os.path

def handleDownload(block):
    file.write(block)
    print ".",

#ddir='C:\\Batches\\Temp\\barclays\\'
#old ddir='C:\\Batches\\AutomationProjects\\Investment Strategy\\Downloads\\barclays\\'
import config
ddir = config.localunprocessedfolder + '\\barclays'

os.chdir(ddir)
ftp = FTP('pcdial.lehman.com')

print 'Logging in.'
ftp.login('advest', 'fred0702')

print 'Accessing files'

#filenames = ftp.nlst() # get filenames within the directory
#print filenames

import datetime

today = datetime.date.today()
print 'today is:', today

iref = -15

while True:
    refdate = today + datetime.timedelta(days=iref)
    refdate8 = str(refdate).replace('-','')
    
    if iref > 0:
        break
    
    print 'Getting files from ',refdate8,'...'    

    for name in ftp.nlst():
            getthis = 0
            if refdate8 in name:
                if name[-4:] == '.agg':
                    getthis = 1                        
                #if name[-5:] == '.aggr':
                #    getthis = 1                        
                #if name[-5:] == '.muni':
                #    getthis = 1 
                #if name[-4:] == '.hyd':
                #    getthis = 1
                #if name[-4:] == '.gcs':
                #    getthis = 1
                #if name[-5:] == '.belw':
                #    getthis = 1

                if getthis != 0:            
                    
                    local_filename = os.path.join(ddir, name)
                    file = open(local_filename, 'wb')
                    ftp.retrbinary('RETR '+ name, file.write)
                    file.close()        
                    print 'retrieved',name
            
    iref = iref + 1

print 'done.'
print 'you can find files here:',ddir

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
DataColumnTitle = 'Durat.'   # can be [DayTot or MTDTot]
fileextension = '.agg'

import mytools
otools = mytools.general()

import config
config.localunprocessedfolder 
config.localprocessedfolder 
config.localuploadsreadyfolder 
config.serveruploadsreadyfolder 

localunprocessedfolder = config.localunprocessedfolder + '\\barclays'
localprocessedfolder = config.localunprocessedfolder + '\\barclays\\Ready for daily processing'
otools.make_sure_path_exists(localunprocessedfolder)
otools.make_sure_path_exists(localprocessedfolder)
#localunprocessedfolder = 'C:\Batches\AutomationProjects\Investment Strategy\ETL\zTest'

localoutputfolder = config.localuploadsreadyfolder
etluploadfolder = config.serveruploadsreadyfolder 

otools.make_sure_path_exists(localoutputfolder)
otools.make_sure_path_exists(etluploadfolder)

#localunprocessedfolder = 'C:\Batches\AutomationProjects\Investment Strategy\ETL\zTest'
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
outputfile = localoutputfolder + '\\barclays upload ' + fileextension[-3:] + ' returnsmonthly ' + filedatetime_string + '.csv'
uploadfile = etluploadfolder + '\\barclays upload ' + fileextension[-3:] + ' returnsmonthly ' + filedatetime_string + '.csv'

import os    
import csv
import re
#localunprocessedfolder = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\Downloads\\barclays\\'

mydict = {}

files = os.listdir(localunprocessedfolder)
for filename in files:
    if filename[-4:] == fileextension:
        localunprocessedcsvpathname = os.path.join(localunprocessedfolder, filename)
        
        '''
        # Read the file
        crs = open(localunprocessedcsvpathname, "r")
        f = open(localunprocessedcsvpathname, 'r')
        all_words = map(lambda l: l.split('\t'), f.readlines())
        for row in all_words:
            print row
        '''
        checkingon = 0
        mycolumn = -1
        with open(localunprocessedcsvpathname, 'r') as f:
            reader = csv.reader(f, dialect='excel', delimiter='\t')
            for row in reader:
                #print len(row),row, 'xxxxxxxx'
                if 'ToWorst' in str(row):
                    if 'Value' in str(row):
                        print 'found ToWorst *******************'
                        mycharindex =  [ (i.start(), i.end()) for i in re.finditer('    Value', str(row))]
                        mycharindex_string = str(mycharindex[0])
                        mycharindex_string = mycharindex_string.replace('(','')
                        mycharindex_string = mycharindex_string.replace(')','')
                        mycharindex_string = mycharindex_string.replace(' ','')
                        mycharindex_start = int(mycharindex_string.split(',')[0])
                        mycharindex_end = int(mycharindex_string.split(',')[1])
                        print mycharindex_start,mycharindex_end,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'
                    
                    checkingon = 1

   
                elif checkingon == 1:
                    mymarketvalue = str(row)[mycharindex_start:mycharindex_end]
                    onlydigits = mymarketvalue.replace(' ','').replace('.','').replace('-','')

                    if checkingon == 1:
                        testsection1 = str(row)[2:len('  Financial Institutio')][:2]
                        #print 'testsection1',testsection1,'11111111111111111111111111111111111111111111111'
                        if testsection1.strip() != '':
                            mysection1 = str(row)[2:len('  Financial Institutio')].strip()
                            mysection1 = mysection1.replace('[','')
                            mysection1 = mysection1.replace(']','')
                            mysection1 = mysection1.replace('\'','')
                            #print mysection1, '@@@@@@@@@@@@@@ Section 1 @@@@@@@@@@@@@@@@'
    
                        testsection2 = str(row)[2:len('  Financial Institutio')][:4]
                        #print 'testsection2',testsection2,'222222222222222222222222222222222222222222222222'
                        if testsection2.strip() != '':
                            mysection2 = str(row)[2:len('  Financial Institutio')].strip()
                            mysection2 = mysection2.replace('[','')
                            mysection2 = mysection2.replace(']','')
                            mysection2 = mysection2.replace('\'','')
                            #print mysection2, '@@@@@@@@@@@@@@ Section 2 @@@@@@@@@@@@@@@@'                  
                      
                  
                  
                    if 'INDEX RESULTS' in str(row):
                        break
                    if len(str(row)) > mycharindex_end:
                        #print str(row)[2:21],str(row)[22:31],str(row)[32:38],mymarketvalue,filename,'|||||',row[0], 'xxxxxxxx', str(row)[32:39]
                        issuename = str(row)[2:len('  Financial Institutio')]
                        issuename = issuename.replace('[','')
                        issuename = issuename.replace(']','')
                        issuename = issuename.replace('\'','')
                        #if not issuename[:2] == '  ':
                        if mymarketvalue.strip().replace('-','').replace('.','').isdigit() == True:
                            if mysection1 == 'U.S. Aggregate' and mysection2 == 'U.S. Aggregate':
                                #print mysection1,mysection2,mymarketvalue.strip(),filename
                                mydict[len(mydict)] = {'source':'barclays','category':'agg','mysection1':mysection1,'mysection2':mysection2,'issue':issuename.strip(),'marketvalue':mymarketvalue.strip(),'filename':filename}

        
        
        
        ## #####################
        ## Moves processed files
        import os
        localprocessedcsvpathname = os.path.join(localprocessedfolder,filename) #'E:\Batches\development\projects\Investment Strategy\ETL\Uploads\Ready'.encode('string_escape')
        #if os.path.exists(localprocessedcsvpathname):
        #    os.remove(localprocessedcsvpathname)
        #shutil.move(localunprocessedcsvpathname, localprocessedfolder)
        ## #####################
                        
    
for k,v in mydict.items():
    print k,v

'''
# ###############################
# Create the csv file
if len(mydict)>0:
    with open(outputfile, 'wb') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, mydict[0].keys(),delimiter = "|")
        w.writeheader()
        for k,v in mydict.items():
            w.writerow(v)
    
    if os.path.exists(uploadfile):
        os.remove(uploadfile)
    shutil.move(outputfile, etluploadfolder)
# ###############################
    print 'You can find your files here:',etluploadfolder
else:
    print 'No files exist or all files were already processed'
'''
