# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 09:42:42 2015

@author: justin.malinchak

Description
"""


# // Parameters
DataColumnTitle = 'MTD Total'   # can be [DayTot or MTDTot]
fileextension = '.gcs'

import config
config.localunprocessedfolder 
config.localprocessedfolder 
config.localuploadsreadyfolder 
config.serveruploadsreadyfolder 


localunprocessedfolder = config.localunprocessedfolder + '\\barclays'
localprocessedfolder = config.localunprocessedfolder + '\\barclays\\Ready for daily processing'
#localunprocessedfolder = 'C:\Batches\AutomationProjects\Investment Strategy\ETL\zTest'

localoutputfolder = config.localuploadsreadyfolder  #'C:\Batches\AutomationProjects\Investment Strategy\ETL\Uploads\Ready'
etluploadfolder = config.serveruploadsreadyfolder  #'E:\\Batches\\development\\projects\\Investment Strategy\\ETL\\Uploads\\Ready'

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
outputfile = localoutputfolder + '\\barclays upload ' + fileextension[(-1)*(len(fileextension)-1):] + ' returnsmonthly ' + filedatetime_string + '.csv'
uploadfile = etluploadfolder + '\\barclays upload ' + fileextension[(-1)*(len(fileextension)-1):] + ' returnsmonthly ' + filedatetime_string + '.csv'

import os    
import csv
import re
#localunprocessedfolder = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\Downloads\\barclays\\'

mydict = {}

files = os.listdir(localunprocessedfolder)
#print files,'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
for filename in files:
    thisfileextension = filename[(-1)*(len(fileextension)):]
    #print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    #print filename
    if thisfileextension == fileextension:
        print 'processing',filename
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
        mycharindex_start = -1
        mycharindex_end = -1
        mysection = ''
        with open(localunprocessedcsvpathname, 'r') as f:
            reader = csv.reader(f, dialect='excel', delimiter='\t')
            currentrow = 0
            checkingon = 0
            for row in reader:
                currentrow = currentrow + 1
                # ================================
                #if currentrow <= 2:
                #print len(row),row, 'xxxxxxxx'
                # ================================
                if DataColumnTitle in str(row):
                    #print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                    #print row
                    #IndexOfMTDTot = row.index(DataColumnTitle)
                    #print IndexOfMTDTot
                    mycharindex =  [ (i.start(), i.end()) for i in re.finditer(DataColumnTitle, str(row))]
                    
                    mycharindex_string = str(mycharindex[0])
                    #print mycharindex_string
                    mycharindex_string = mycharindex_string.replace('(','')
                    mycharindex_string = mycharindex_string.replace(')','')
                    mycharindex_string = mycharindex_string.replace(' ','')
                    mycharindex_start = int(mycharindex_string.split(',')[0])
                    mycharindex_end = int(mycharindex_string.split(',')[1])
                    #print mycharindex_start,mycharindex_end,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'
                    checkingon = 1
                if checkingon == 1 and ':' in str(row) and len(str(row)) < 40:
                    
                    mysection = str(row[0]).replace(':','')
                    #print row[0], '@@@@@@@@@@@@@@ Section @@@@@@@@@@@@@@@@'
                if checkingon == 1 and len(str(row)) > mycharindex_end:
                    #print 'ok on',row[1]
                    #print 'checking is on',row,mycharindex_start,mycharindex_end
                    #mymtdreturn = row[IndexOfMTDTot]
                    
                    mymtdreturn = str(row)[mycharindex_start:mycharindex_end]
                    
                    onlydigits = mymtdreturn.replace(' ','').replace('.','').replace('-','')
                    if onlydigits.isdigit():
                        #print str(row)
                        #print mycharindex_start
                        #print mycharindex_end
                        issuename = str(row)[2:len('                                             ')]
                        #print issuename,mymtdreturn,filename
                        mydict[len(mydict)] = {'source':'barclays','DataColumnTitle':DataColumnTitle,'category':'gcs','section':mysection,'issue':issuename.strip(),'mtdtotalreturn':mymtdreturn.strip(),'filename':filename}
                        #print str(row)
                    elif mymtdreturn.strip() == 'MTD Total':
                        dummyvariable = True
#                        print mymtdreturn.strip()
#                        print '=================================================================================='
#                        print str(row)
                    elif mymtdreturn.strip() == 'Return':
                        dummyvariable = True
                        #print mymtdreturn.strip(),'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'                        
                    else:
                        #print mymtdreturn.strip(),'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
                        checkingon = 0
        
        import os
        #import shutil
        #root_src_dir = localunprocessedfolder #'C:\Batches\AutomationProjects\Investment Strategy\ETL\Uploads\Ready'.encode('string_escape')
        #root_dst_dir = 'C:\Batches\AutomationProjects\Investment Strategy\ETL\Uploads\Complete'.encode('string_escape')
        localprocessedcsvpathname = os.path.join(localprocessedfolder,filename) #'E:\Batches\development\projects\Investment Strategy\ETL\Uploads\Ready'.encode('string_escape')
        if os.path.exists(localprocessedcsvpathname):
            os.remove(localprocessedcsvpathname)
        shutil.move(localunprocessedcsvpathname, localprocessedfolder)

         #os.path.join(localprocessedfolder,filename) #'E:\Batches\development\projects\Investment Strategy\ETL\Uploads\Ready'.encode('string_escape')

#for k,v in mydict.items():
#    print k,v
        
        
#
if len(mydict) > 0:
    with open(outputfile, 'wb') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, mydict[0].keys(),delimiter = "|")
        w.writeheader()
        for k,v in mydict.items():
            w.writerow(v)
            print v
    
    if os.path.exists(uploadfile):
        os.remove(uploadfile)
    shutil.move(outputfile, etluploadfolder)
    
    print 'you can find your file on network here:', uploadfile
else:
    print 'no files created'
# =============================
# when you're ready to upload file, enable this...
#
# copyFile(outputfile, uploadfile)
#
# =============================