# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 09:42:42 2015

@author: justin.malinchak

Description
"""


# // Parameters
DataColumnTitle = '    Since'   # can be [DayTot or MTDTot]
DataColumSecondRow = 'Inception'
fileextension = '.gcs'
import config
config.localunprocessedfolder 
config.localprocessedfolder 
config.localuploadsreadyfolder 
config.serveruploadsreadyfolder 

localunprocessedfolder = config.localunprocessedfolder+'\\barclays'
localprocessedfolder = config.localunprocessedfolder+'\\barclays\\Ready for daily processing'
#localunprocessedfolder = 'C:\Batches\AutomationProjects\Investment Strategy\ETL\zTest'

localoutputfolder = config.localuploadsreadyfolder #'C:\Batches\AutomationProjects\Investment Strategy\ETL\Uploads\Ready'
etluploadfolder = config.serveruploadsreadyfolder #'E:\\Batches\\development\\projects\\Investment Strategy\\ETL\\Uploads\\Ready'

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
import mytools
mytools.general().make_sure_path_exists(localprocessedfolder)
import datetime
filedatetime = datetime.datetime.today()
filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S%M')
outputfile = localoutputfolder + '\\barclays upload ' + fileextension[(-1)*(len(fileextension)-1):] + ' sinceinception ' + filedatetime_string + '.csv'
uploadfile = etluploadfolder + '\\barclays upload ' + fileextension[(-1)*(len(fileextension)-1):] + ' sinceinception ' + filedatetime_string + '.csv'

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
                    print '+ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
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
                    #mydatavalue = row[IndexOfMTDTot]
                    
                    mydatavalue = str(row)[mycharindex_start:mycharindex_end]
                    print 'mydatavalue',mydatavalue
                    onlydigits = mydatavalue.replace(' ','').replace('.','').replace('-','')
                    if onlydigits.isdigit():
                        #print str(row)
                        #print mycharindex_start
                        #print mycharindex_end
                        issuename = str(row)[2:len('                                             ')]
                        print 'issuename',issuename,mydatavalue,filename
                        mydict[len(mydict)] = {'source':'barclays','DataColumnTitle':DataColumnTitle.strip() + ' ' + DataColumSecondRow.strip(),'category':'gcs','section':mysection,'issue':issuename.strip(),'mydatavalue':mydatavalue.strip(),'filename':filename}
                        #print str(row)
                    elif mydatavalue.strip() == DataColumnTitle.strip():
                        dummyvariable = True
#                        print mydatavalue.strip()
#                        print '=================================================================================='
#                        print str(row)
                    elif mydatavalue.strip() == DataColumSecondRow:
                        dummyvariable = True
                        #print mydatavalue.strip(),'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'                        
                    else:
                        #print mydatavalue.strip(),'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
                        print 'checking shut off'
                        checkingon = 0
        
        
#        # ##############################################
#        # Disable for development, enable for production
#        import os
#        localprocessedcsvpathname = os.path.join(localprocessedfolder,filename) #'E:\Batches\development\projects\Investment Strategy\ETL\Uploads\Ready'.encode('string_escape')
#        if os.path.exists(localprocessedcsvpathname):
#            os.remove(localprocessedcsvpathname)
#        shutil.move(localunprocessedcsvpathname, localprocessedfolder)
#        # ##############################################
         
         #os.path.join(localprocessedfolder,filename) #'E:\Batches\development\projects\Investment Strategy\ETL\Uploads\Ready'.encode('string_escape')

#for k,v in mydict.items():
#    print k,v
        
        
#
if len(mydict) == 0:
    print('No records to process, possibly no '+fileextension+' files found.')
else:
    with open(outputfile, 'wb') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, mydict[0].keys(),delimiter = "|")
        w.writeheader()
        for k,v in mydict.items():
            w.writerow(v)
            print v
    
    # ##############################################
    # Disable for development, enable for production
    if os.path.exists(uploadfile):
        os.remove(uploadfile)
    shutil.move(outputfile, etluploadfolder)
    # ##############################################
    
    print 'you can find your file on network here:', uploadfile

# =============================
# when you're ready to upload file, enable this...
#
# copyFile(outputfile, uploadfile)
#
# =============================