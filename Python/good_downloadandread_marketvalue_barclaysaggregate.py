'''
# Notes
    Downloads last 5 days of Barclays data from lehman via ftp
'''
#################################################################################
download_last_x_days = -5
#################################################################################

from ftplib import FTP
import os, os.path

def handleDownload(block):
    file.write(block)
    print ".",

#directory_where_datafiles_are_downloaded='C:\\Batches\\Temp\\barclays\\'
#old directory_where_datafiles_are_downloaded='C:\\Batches\\AutomationProjects\\Investment Strategy\\Downloads\\barclays\\'

import config
directory_where_datafiles_are_downloaded = os.path.join(config.localunprocessedfolder,'barclays')

os.chdir(directory_where_datafiles_are_downloaded)
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

iref = download_last_x_days

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
                    
                    local_filename = os.path.join(directory_where_datafiles_are_downloaded, name)
                    file = open(local_filename, 'wb')
                    ftp.retrbinary('RETR '+ name, file.write)
                    file.close()        
                    print 'retrieved',name
            
    

print 'downloading of files is done.'
print 'you can find files here:',directory_where_datafiles_are_downloaded

#################################################################################

#################################################################################
import config
import os
import good_readvalues_marketvalue_barclays_aggregate as ofile
pclass = ofile.perform()
newdata_dict = pclass.execute(download_last_x_days,directory_where_datafiles_are_downloaded)

import datetime
filedatetime = datetime.datetime.today()
filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S')

# Get path of savedjsonfile
savedjsonfile = os.path.join(config.localdatafileoutputpath,'dailyreturns-barclays-usaggregate.json')

def create_saved_dict(p_savedjsonfile):
    import json
    saved_dict = {}
    try:
        with open(p_savedjsonfile) as f:
            saved_dict = json.load(f)
    except Exception as e:
        print 'error: just created a new saved_dict'
    return saved_dict

        
import json
if os.path.isfile(savedjsonfile) == True:
    print 'got here 1'
    # Read file with previously saved data into dictionary
    saved_dict = create_saved_dict(savedjsonfile)
    print len(saved_dict)
    # Create a copy of saved_dict, call it updated_dict and update it with newdata_dict
    updated_dict = saved_dict.copy()
    updated_dict.update(newdata_dict)
else:
    print 'got here 2'
    updated_dict = newdata_dict

# save updated_dict to savedjsonfile
#import json
with open(savedjsonfile, 'w') as f:
    json.dump(updated_dict, f)

# open savedjsonfile into testing_dict, and print key values to screen
with open(savedjsonfile) as f:
    testing_dict = json.load(f)
for key, value in sorted(testing_dict.iteritems()):
    print value['currdate'],value['periodreturn'], value['filedatetime']


print 'You can find your file here:',savedjsonfile

