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
iref = -30
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

#################################################################################################

marketvalues_dict = {}

import datetime

today = datetime.date.today()
print 'today is:', today

dict_of_date8s = {}
#iref = -15
while True:
    if iref > 0:
        break
    refdate = today + datetime.timedelta(days=iref)
    refdate8 = str(refdate).replace('-','')
    dict_of_date8s[len(dict_of_date8s)] = refdate8
    iref = iref + 1

for key, value in sorted(dict_of_date8s.iteritems()):
    #print(key, value)

    myfile = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\\Downloads\\Unprocessed\\barclays\\'+value+'.agg'
    import os
    import good_readvalue_marketvalue_barclays_aggregate as o
    p = o.perform()
    mydict = p.execute(myfile)
    for k,v in mydict.items():
        #print k,v
        #print v
        date8 = os.path.basename(v['filename'])[:8]
        marketvalue = v['marketvalue']
        marketvalues_dict[date8] = marketvalue
prevmv = -1
returns_dict = {}
for key, value in sorted(marketvalues_dict.iteritems()):
    currmv = float(value)
    #print(key, prevmv,currmv)
    if prevmv > 0:
        periodreturn = (currmv - prevmv) / prevmv
        returns_dict[key] = [prevmv,currmv,periodreturn]
    prevmv = currmv
    
for key, value in sorted(returns_dict.iteritems()):
    print key,value

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
