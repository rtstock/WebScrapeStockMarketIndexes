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
DataColumnTitle = '    Since'   # can be [DayTot or MTDTot]
DataColumnSecondRow = 'Inception'
fileextension = '.hyd'

import config
config.localunprocessedfolder 
config.localprocessedfolder 
config.localuploadsreadyfolder 
config.serveruploadsreadyfolder 

localunprocessedfolder = config.localunprocessedfolder +'\\barclays'
localprocessedfolder = config.localunprocessedfolder +'\\barclays\\Ready for daily processing'
#localunprocessedfolder = 'C:\Batches\AutomationProjects\Investment Strategy\ETL\zTest'

localoutputfolder = 'C:\Batches\AutomationProjects\Investment Strategy\ETL\Uploads\Ready'
etluploadfolder = 'E:\\Batches\\development\\projects\\Investment Strategy\\ETL\\Uploads\\Ready'

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
outputfile = localoutputfolder + '\\barclays upload ' + fileextension[-3:] + ' sinceinception ' + filedatetime_string + '.csv'
uploadfile = etluploadfolder + '\\barclays upload ' + fileextension[-3:] + ' sinceinception ' + filedatetime_string + '.csv'

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

                if DataColumnTitle in str(row):
                    print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                    mycharindex =  [ (i.start(), i.end()) for i in re.finditer(DataColumnTitle, str(row))]
                    mycharindex_string = str(mycharindex[0])
                    mycharindex_string = mycharindex_string.replace('(','')
                    mycharindex_string = mycharindex_string.replace(')','')
                    mycharindex_string = mycharindex_string.replace(' ','')
                    mycharindex_start = int(mycharindex_string.split(',')[0])
                    mycharindex_end = int(mycharindex_string.split(',')[1])
                    #print mycharindex_start,mycharindex_end,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'
                    
                    checkingon = 1

   
                elif checkingon == 1:
                    mydatavalue = str(row)[mycharindex_start:mycharindex_end]
                    onlydigits = mydatavalue.replace(' ','').replace('.','').replace('-','')

                    if checkingon == 1:
                        testsection1 = str(row)[2:len('  U.S. Corporate High Y')][:2]
                        #print 'testsection1',testsection1,'11111111111111111111111111111111111111111111111'
                        if testsection1.strip() != '':
                            mysection1 = str(row)[2:len('  U.S. Corporate High Y')].strip()
                            print mysection1, '@@@@@@@@@@@@@@ Section 1 @@@@@@@@@@@@@@@@'
    
                        testsection2 = str(row)[2:len('  U.S. Corporate High Y')][:4]
                        #print 'testsection2',testsection2,'222222222222222222222222222222222222222222222222'
                        if testsection2.strip() != '':
                            mysection2 = str(row)[2:len('  U.S. Corporate High Y')].strip()
                            print mysection2, '@@@@@@@@@@@@@@ Section 2 @@@@@@@@@@@@@@@@'                  
                      
                  
                  
                    if 'Durat.' in str(row):
                        break
                    if len(str(row)) > mycharindex_end:
                        #print str(row)[2:21],str(row)[22:31],str(row)[32:38],mydatavalue,filename,'|||||',row[0], 'xxxxxxxx', str(row)[32:39]
                        issuename = str(row)[2:len('  U.S. Corporate High Y')]
                        #if not issuename[:2] == '  ':
                        if mydatavalue.strip().replace('-','').replace('.','').isdigit() == True:
                            mydict[len(mydict)] = {'source':'barclays','category':'hyd','mysection1':mysection1,'mysection2':mysection2,'issue':issuename.strip(),'datavalue':mydatavalue.strip(),'filename':filename}

        
        
        
#        # #####################
#        # Moves processed files
#        import os
#        localprocessedcsvpathname = os.path.join(localprocessedfolder,filename) #'E:\Batches\development\projects\Investment Strategy\ETL\Uploads\Ready'.encode('string_escape')
#        if os.path.exists(localprocessedcsvpathname):
#            os.remove(localprocessedcsvpathname)
#        shutil.move(localunprocessedcsvpathname, localprocessedfolder)
#        # #####################
                        
    
for k,v in mydict.items():
    print k,v

if len(mydict) == 0:
    print('No records to process, possibly no '+fileextension+' files found.')
else:
    # ###############################
    # Create the csv file
    with open(outputfile, 'wb') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, mydict[0].keys(),delimiter = "|")
        w.writeheader()
        for k,v in mydict.items():
            w.writerow(v)
    
    if os.path.exists(uploadfile):
        os.remove(uploadfile)
    shutil.move(outputfile, etluploadfolder)

# ###############################

