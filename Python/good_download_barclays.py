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
ddir= config.localunprocessedfolder +'\\barclays'
os.chdir(ddir)
ftp = FTP('pcdial.lehman.com')
print 'Started process to download Barclays'
print 'Logging in.'
ftp.login('advest', 'fred0702')
#directory = '\\data\\test\\'

#print 'Changing to ' + directory
#ftp.cwd(directory)
#ftp.retrlines('LIST')

print 'Accessing files'

#filenames = ftp.nlst() # get filenames within the directory
#print filenames

import datetime


today = datetime.date.today()
print 'today is:', today

iref = -5

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
                if name[-5:] == '.aggr':
                    getthis = 1                        
                if name[-5:] == '.muni':
                    getthis = 1 
                if name[-4:] == '.hyd':
                    getthis = 1
                if name[-4:] == '.gcs':
                    getthis = 1
                if getthis != 0:            
                    
                    local_filename = os.path.join(ddir, name)
                    file = open(local_filename, 'wb')
                    ftp.retrbinary('RETR '+ name, file.write)
                    file.close()        
                    print 'retrieved',name
            
    iref = iref + 1

print 'done.'
print 'you can find files here:',ddir