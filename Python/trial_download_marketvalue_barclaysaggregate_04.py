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

dict_of_date8s = {}
iref = -5
while True:
    if iref > 0:
        break
    refdate = today + datetime.timedelta(days=iref)
    refdate8 = str(refdate).replace('-','')
    dict_of_date8s[len(dict_of_date8s)] = refdate8
    iref = iref + 1

for key, value in sorted(dict_of_date8s.iteritems()):
    print(key, value)


for k,refdate8 in sorted(dict_of_date8s.iteritems()):
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
            
    

print 'done.'
print 'you can find files here:',ddir
#################################################################################
import config

import os
import good_readvalues_marketvalue_barclays_aggregate as o

#print config.localunprocessedfolder
#localunprocessedfolderext = os.path.join(config.localunprocessedfolder,'barclays')

p = o.perform()
mydict = p.execute(iref,ddir)

for key, value in sorted(mydict.iteritems()):
    print key,value

