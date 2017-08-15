# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 09:42:42 2015

@author: justin.malinchak

Description
"""


# // Parameters
PageMarker = 'Page 2'
datacolumntitle_marketvalue = '    Value'
datacolumntitle_price = '  Price'
fileextension = '.gcs'

import config
config.localunprocessedfolder 
config.localprocessedfolder 
config.localuploadsreadyfolder 
config.serveruploadsreadyfolder 

localoutputfolder = config.localuploadsreadyfolder  #'C:\Batches\AutomationProjects\Investment Strategy\ETL\Uploads\Ready'
etluploadfolder = config.serveruploadsreadyfolder  #'E:\\Batches\\development\\projects\\Investment Strategy\\ETL\\Uploads\\Ready'

#localunprocessedfolder = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\Downloads\\Unprocessed\\barclays'
localunprocessedfolder = config.localunprocessedfolder + '\\barclays\\Ready for daily processing'
localprocessedfolder = config.localprocessedfolder + '\\barclays'
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
outputfile = localoutputfolder + '\\barclays upload ' + fileextension[(-1)*(len(fileextension)-1):] + ' priceandmarketvalue ' + filedatetime_string + '.csv'
uploadfile = etluploadfolder + '\\barclays upload ' + fileextension[(-1)*(len(fileextension)-1):] + ' priceandmarketvalue ' + filedatetime_string + '.csv'

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
        mycharindex_marketvalue_start = -1
        mycharindex_marketvalue_end = -1
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
                if PageMarker in str(row):
                    print 'checking set to on ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                    print str(row)
                    #print row
                    #IndexOfMTDTot = row.index(datacolumntitle_marketvalue)
                    #print IndexOfMTDTot
                    #print mycharindex_marketvalue_start,mycharindex_marketvalue_end,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'
                    checkingon = 1
                elif checkingon == 1 and mycharindex_marketvalue_start < 0:
                    #print str(row).strip()[-40:]
                    if datacolumntitle_marketvalue in str(row).strip()[-40:]:
                        print 'datacolumntitle_marketvalue',datacolumntitle_marketvalue,'found !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                        mycharindex =  [ (i.start(), i.end()) for i in re.finditer(datacolumntitle_marketvalue, str(row))]
                        
                        mycharindex_marketvalue_string = str(mycharindex[0])
                        
                        mycharindex_marketvalue_string = mycharindex_marketvalue_string.replace('(','')
                        mycharindex_marketvalue_string = mycharindex_marketvalue_string.replace(')','')
                        mycharindex_marketvalue_string = mycharindex_marketvalue_string.replace(' ','')
                        mycharindex_marketvalue_start = int(mycharindex_marketvalue_string.split(',')[0])
                        mycharindex_marketvalue_end = int(mycharindex_marketvalue_string.split(',')[1])
                        print mycharindex_marketvalue_start,mycharindex_marketvalue_end
                    if datacolumntitle_price in str(row).strip()[-60:]:
                        print 'datacolumntitle_price',datacolumntitle_price,'found !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                        mycharindex =  [ (i.start(), i.end()) for i in re.finditer(datacolumntitle_price, str(row))]
                        
                        mycharindex_price_string = str(mycharindex[0])
                        
                        mycharindex_price_string = mycharindex_price_string.replace('(','')
                        mycharindex_price_string = mycharindex_price_string.replace(')','')
                        mycharindex_price_string = mycharindex_price_string.replace(' ','')
                        mycharindex_price_start = int(mycharindex_price_string.split(',')[0])
                        mycharindex_price_end = int(mycharindex_price_string.split(',')[1])
                        print mycharindex_price_start,mycharindex_price_end
                        
                elif checkingon == 1 and mycharindex_marketvalue_start > 0:
                    #print str(row)
                    if ':' in str(row) and len(str(row).strip()) < 40:
                        mysection = str(row[0]).replace(':','')
                        print mysection, '@@@@@@@@@@@@@@ Section @@@@@@@@@@@@@@@@'
                mymarketvalue = ''
                myprice = ''
                if checkingon == 1 and len(mysection) > 0 and len(str(row)) > mycharindex_marketvalue_end:
                    mymarketvalue = str(row)[mycharindex_marketvalue_start:mycharindex_marketvalue_end]                    
                    onlydigits_marketvalue = mymarketvalue.replace(' ','').replace('.','').replace('-','')
                    if mymarketvalue.strip() == '':
                        mymarketvalue = ''
                        dummyvariable = True
                    elif onlydigits_marketvalue.isdigit():
                        mymarketvalue = mymarketvalue.strip()
                        dummyvariable = False
                    else:
                        checkingon = 0

                if checkingon == 1 and len(mysection) > 0 and len(str(row)) > mycharindex_price_end:
                    myprice = str(row)[mycharindex_price_start:mycharindex_price_end]                    
                    onlydigits_price = myprice.replace(' ','').replace('.','').replace('-','')
                    if myprice.strip() == '':
                        myprice = ''
                        dummyvariable = True
                    elif onlydigits_price.isdigit():
                        myprice = myprice.strip()
                        dummyvariable = False
                    else:
                        checkingon = 0
                
                if len(mymarketvalue) > 0 and len(myprice) > 0:
                    issuename = str(row)[2:len('Intermediate Gov/Credit + MBS                  ')]
                    mydict[len(mydict)] = {'source':'barclays','category':'gcs','section':mysection,'issue':issuename.strip(),'myprice':myprice,'mymarketvalue':mymarketvalue,'filename':filename}

        import os
        localprocessedcsvpathname = os.path.join(localprocessedfolder,filename) #'E:\Batches\development\projects\Investment Strategy\ETL\Uploads\Ready'.encode('string_escape')
        if os.path.exists(localprocessedcsvpathname):
            os.remove(localprocessedcsvpathname)
        shutil.move(localunprocessedcsvpathname, localprocessedfolder)


for k,v in mydict.items():
    print k,v
        
        
print 'length of my dict', len(mydict)
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
    print 'You can find you file here:',etluploadfolder
else:
    print 'No files created'

#print 'you can find your file on network here:', uploadfile

# =============================
# when you're ready to upload file, enable this...
#
# copyFile(outputfile, uploadfile)
#
# =============================