
from ftplib import FTP
import os, sys, os.path

def handleDownload(block):
    file.write(block)
    print ".",

ddir='C:\\Batches\\Temp\\barclays\\'
os.chdir(ddir)
ftp = FTP('pcdial.lehman.com')

print 'Logging in.'
ftp.login('advest', 'fred0702')
#directory = '\\data\\test\\'

#print 'Changing to ' + directory
#ftp.cwd(directory)
#ftp.retrlines('LIST')

print 'Accessing files'

#filenames = ftp.nlst() # get filenames within the directory
#print filenames


for name in ftp.nlst():
        getthis = 0
    #if '20150529' in name:
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
            print 'ok',name
        
        
        
        
        
        
        #ftp.cwd(name)
        #print ftp.pwd()
        #ftp.nlst()

#import fnmatch
##lst = ['this','is','just','a','test']
#filtered = fnmatch.filter(filenames, '*20150515*')
#print filtered

#import re
#regex = re.compile('20150531')
##newlist = ['this', 'is', 'just', 'a', 'test']
#matches = [string for string in filenames if re.match(regex, string)]
#print matches

#
#for filename in filenames:
#    local_filename = os.path.join(ddir, filename)
#    file = open(local_filename, 'wb')
#    ftp.retrbinary('RETR '+ filename, file.write)
#    file.close()
#ftp.quit()