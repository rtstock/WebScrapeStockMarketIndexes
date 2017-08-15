# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 10:50:44 2015

@author: justin.malinchak

------------
Description:
------------
    Downloads HRFX data for whatever data is available on their website when the process is executed.
    The output of this process is a pipe delimited csv and should be used for bulk loading into SQL

"""

# ==========
# Parameters

url = 'http://slickcharts.com/sp500'

import config
localoutputfolder = config.localuploadsreadyfolder
etluploadfolder = config.serveruploadsreadyfolder

#localoutputfolder = 'C:\Batches\AutomationProjects\Investment Strategy\ETL\Uploads\Ready'
#etluploadfolder = 'E:\\Batches\\development\\projects\\Investment Strategy\\ETL\\Uploads\\Ready'

import shutil

def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False

    return True

def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)

def CheckDate(DateString,DateFormat):
    import time
    date = DateString
    try:
      valid_date = time.strptime(date, DateFormat)
      valid_date = valid_date
      #print DateString,'is a valid date!'
      #print valid_date
      return True
    except ValueError:
      #print DateString,'is not a valid date'
      return False

import datetime
from datetime import timedelta
filedatetime = datetime.datetime.today()
filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S%M')
lastMonthEndDate  = datetime.date(datetime.datetime.today().year,datetime.datetime.today().month,1) - timedelta(days=1)
lastMonthEndDateString = str(lastMonthEndDate).replace('-','')
print('lastMonthEndDate',str(lastMonthEndDate))

outputfile = localoutputfolder + '\\sp500weights upload ' + filedatetime_string + '.csv'
uploadfile = etluploadfolder + '\\sp500weights upload ' + filedatetime_string + '.csv'


try:
  
    # website - DM gross        Market:DM IndexLevel:Gross Size:Standard                        Example: hfrx THE WORLD INDEX	hfrxWD	3/31/2015	-1.50
    #url = 'https://app.hfrx.com/webapp/indexperf/excel?scope=0&priceLevel=40&market=1897&style=C&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
    
    #url = 'http://www.hfrx.com/indexcalculator/IndexCalculator/api/index/cumulative/302/1/'+lastMonthEndDateString+'/1?_dc=1433956529495'
    #lastMonthEndDateString

    from bs4 import BeautifulSoup
    import urllib2
    #url="http://www.99acres.com/property-in-velachery-chennai-south-ffid?"
    page=urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    #print soup
    #if MySearchString in str(soup):
    #    print 'Yesssssssssssssssssssssssssssssss'
    bodies = [a.get_text() for a in soup.find_all('body')]
    fonts = [a.get_text() for a in soup.find_all('font')]
    
    #print '-------------------bodies',bodies
    #print '-------------------fonts',fonts
    #print '================================================================='
    mydict = {}
    bFoundMark = 0
    mydict = {}
    idict = 0
    for x in bodies:
        #print '----'
        #print x
        #guggenhiem
        y = x.split('\n')
        #print y
        for z in y:
            if z == 'Components of the S&P 500':
                bFoundMark = 1
            if 'SlickCharts.com' in z:
                bFoundMark = 0
            if bFoundMark == 1:
                mystring = z.rstrip(' ')
                mystring = z.lstrip(' ')
                if len(mystring)>0:
                    
                    if not is_number(mystring) == 1:
                        idict += 1
                        myname = mystring
                    else:
                        if len(myname) > 0:
                            mynumber = float(mystring)
                            mydict[idict] = {'AsOf': filedatetime.strftime('%Y-%m-%d'),'Name':myname,'Value':mynumber}

    #print mydict()                
                        
        #print '----'   
        #print y
        #z = y[0].split('\\')
        #print z
        #for a in z:
        #    print '----'
        #    print a
        
except StopIteration:
  raise
except Exception as e:
  print(e) # or whatever kind of logging you want
  pass

        
#for k,v in mydict.items():
#    print k,v

print 'outputfile',outputfile
#print 'mydict.keys()', mydict.keys()
headings = ['AsOf','Name','Value']
import csv
with open(outputfile, 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, fieldnames=headings, dialect='excel', quoting=csv.QUOTE_NONNUMERIC) #,delimiter = "|"
    w.writeheader()
    for k,v in mydict.items():
        w.writerow(v)
  
copyFile(outputfile, uploadfile)
      
##
print 'you can find your file locally here:', outputfile
print 'you can find your file on the sql server filesystem here:', uploadfile
