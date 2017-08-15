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

fileextension = '.muni'

import config
config.localunprocessedfolder 
config.localprocessedfolder 
config.localuploadsreadyfolder 
config.serveruploadsreadyfolder 

#localunprocessedfolder = 'C:\Batches\AutomationProjects\Investment Strategy\ETL\zTest'
localunprocessedfolder = config.localunprocessedfolder+'\\barclays'
localprocessedfolder = config.localprocessedfolder+'\\barclays'

localoutputfolder = config.localuploadsreadyfolder #'C:\Batches\AutomationProjects\Investment Strategy\ETL\Uploads\Ready'
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

#import datetime
#filedatetime = datetime.datetime.today()
#filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S%M')
#outputfile = localoutputfolder + '\\barclays upload ' + fileextension[(-1)*(len(fileextension)-1):] + ' ' + filedatetime_string + '.csv'
#uploadfile = etluploadfolder + '\\barclays upload ' + fileextension[(-1)*(len(fileextension)-1):] + ' ' + filedatetime_string + '.csv'


datacolumntitles = ['IncpTot','MktVal','Price']

import datetime
filedatetime = datetime.datetime.today()
filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S%M')
outputfile = localoutputfolder + '\\barclays upload ' + fileextension[(-1)*(len(fileextension)-1):] + ' sinceinceptionpriceandmarketvalue ' + filedatetime_string + '.csv'
uploadfile = etluploadfolder + '\\barclays upload ' + fileextension[(-1)*(len(fileextension)-1):] + ' sinceinceptionpriceandmarketvalue ' + filedatetime_string + '.csv'

import os    
import csv
#import re
#localunprocessedfolder = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\Downloads\\barclays\\'

mydict = {}

files = os.listdir(localunprocessedfolder)
#print files,'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
print 'checking localunprocessedfolder: ',localunprocessedfolder
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
        
        for datacolumntitle in datacolumntitles:
            with open(localunprocessedcsvpathname, 'r') as f:
                reader = csv.reader(f, dialect='excel', delimiter='\t')
                currentrow = 0
                IndexOfString = -1
                for row in reader:
                    currentrow = currentrow + 1
                    # ================================
                    #if currentrow <= 2:
                    #    print len(row),row, 'xxxxxxxx'
                    # ================================
        
                    if datacolumntitle in str(row):
                        #print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                        #print row
                        IndexOfString = row.index(datacolumntitle)
                        #print IndexOfString
    
                        checkingon = 1
                        
                    if checkingon == 1 and IndexOfString > 0 and len(row) > IndexOfString:
                        #print 'ok on',row[1]
                        #print row
                        mydatavalue = row[IndexOfString]
                        
                        onlydigits = mydatavalue.replace(' ','').replace('.','').replace('-','')
                        if onlydigits.isdigit():
                            #print row[0],row[1],row[2],mydatavalue
                            mydict[len(mydict)] = {'source':'BARCLAYS','measure':datacolumntitle,'product':fileextension,'id':row[0].strip(),'name':row[1],'period':row[2],'datavalue':mydatavalue,'filename':filename}
        
#        # #####################
#        # Do not enable this for muni, must 3 processes on files for 3 measures (IncpTot,MktVal,Price)
#        # Move unprocessed file to processed folder
#        import os
#        localprocessedcsvpathname = os.path.join(localprocessedfolder,filename) #'E:\Batches\development\projects\Investment Strategy\ETL\Uploads\Ready'.encode('string_escape')
#        if os.path.exists(localprocessedcsvpathname):
#            os.remove(localprocessedcsvpathname)
#        shutil.move(localunprocessedcsvpathname, localprocessedfolder)
#        # #####################

for k,v in mydict.items():
    print k,v
    
# ##################################
# Enable this for saving data to csv
if len(mydict) == 0:
    print('No records to process, possibly no '+fileextension+' files found.')
else:
    with open(outputfile, 'wb') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, mydict[0].keys(),delimiter = "|")
        w.writeheader()
        for k,v in mydict.items():
            w.writerow(v)

    if os.path.exists(uploadfile):
        os.remove(uploadfile)
    shutil.move(outputfile, etluploadfolder)

    print 'you can find your file locally here:', outputfile
# #####################################


#        
# =============================
# when you're ready to upload file, enable this...
#
#copyFile(outputfile, uploadfile)
#
# =============================