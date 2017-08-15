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
TupleOfSearchStrings = ('HFRX Global Hedge Fund Index','HFRX Equity Hedge Index')
#url = 'https://www.hedgefundresearch.com/hfrx_daily_tickercontent.txt'
url = 'https://www.hedgefundresearch.com/hfrx_reg/index.php?fuse=login&hi'
#url = 'https://www.hedgefundresearch.com/hfrx_reg/index.php?fuse=login_bd'
#url = 'https://www.hedgefundresearch.com/hfrx_reg/TOUPROC.php'


localoutputfolder = 'C:\Batches\AutomationProjects\Investment Strategy\ETL\Uploads\Ready'
etluploadfolder = 'E:\\Batches\\development\\projects\\Investment Strategy\\ETL\\Uploads\\Ready'

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


outputfile = localoutputfolder + '\\try hfrx upload ' + filedatetime_string + '.csv'
uploadfile = etluploadfolder + '\\try hfrx upload ' + filedatetime_string + '.csv'


try:
  
    # website - DM gross        Market:DM IndexLevel:Gross Size:Standard                        Example: hfrx THE WORLD INDEX	hfrxWD	3/31/2015	-1.50
    #url = 'https://app.hfrx.com/webapp/indexperf/excel?scope=0&priceLevel=40&market=1897&style=C&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
    
    #url = 'http://www.hfrx.com/indexcalculator/IndexCalculator/api/index/cumulative/302/1/'+lastMonthEndDateString+'/1?_dc=1433956529495'
    #lastMonthEndDateString

    #from bs4 import BeautifulSoup
    #import urllib2
    #url="http://www.99acres.com/property-in-velachery-chennai-south-ffid?"
    #page=urllib2.urlopen(url)


    import requests
    requests.packages.urllib3.disable_warnings() 
    
#    <input name="username" type="hidden" value="IP Only"/>
#    <input name="ipaddress" type="hidden" value="208.115.45.225"/>
#    <input name="tou_version" type="hidden" value="INDXTOU04012014"/>
#    <input name="page" type="hidden" value="HFRX"/>
#    <input checked="" name="accept" type="radio" value="1"/> <b>I have read, understand and accept these terms of use</b> <br/><br/>
#    <input name="accept" type="radio" value="2"/> I DECLINE<br/><br/>
#    <input align="center" class="submit" name="login" type="submit" value="Submit"/><br/><br/>

    r=requests.post(url,data={'username':'IP Only','ipaddress':'208.115.45.225','tou_version':'INDXTOU04012014','page':'HFRX','checked':'1'})
    print r.text
    
#    soup = BeautifulSoup(page.read())
#    select = soup.find('table',{'id':"tp_section_1"})
    
#    with open('$test.txt', 'w') as f:
#        for section in soup.findAll("p"):
#            print section
#            f.writelines(str(section))
#            f.writelines('++++++++++++++++++++++++++++++++++++++++++++++++++++++')
#    
#        #if 'Submit' in str(section):
#        #    print section
#        
#        #for post in section.findAll('a', attrs={'class':['package-link']}):
#        #    print post
#    
#    bodies = [a.get_text() for a in soup.find_all('tbody')]
#    fonts = [a.get_text() for a in soup.find_all('font')]
#
#    #with open('$test.txt', 'w') as f:
#    #    for x in bodies:            
#    #        x = x.encode("ascii", "ignore")
#    #        #print x
#    #        f.writelines(str(x) + ' ')
#
#    
#    #print '-------------------bodies',bodies
#    #print '-------------------fonts',fonts
#    #print '================================================================='
#    mydict = {}
#    for tupitem in TupleOfSearchStrings:
#        MySearchString = tupitem
#        #print MySearchString
#        #print len(bodies)
#        for x in bodies:
#            
#            x = x.encode("ascii", "ignore")
            #print x
            #if '2.07' in str(x):                
            #    print 'found it'
#                y = str(x).encode('string-escape').split("\\x")
#                print y
#                z = y[0].split('\\')
#                #print z
#                for a in z:
#                    if MySearchString in str(a):   
#                        AsOfDateString = 'n/a'
#                        b = a.replace(MySearchString,'')
#                        c = b.split('%')
#                        #print c
#                        for a1 in c:
#                            #print a1
#                            b1 = a1.split(':')
#                            #print b1
#                            if len(b1) >= 2:
#                                col1 = b1[0].strip()
#                                if CheckDate(col1.replace('n',''),'%Y-%m-%d'):
#                                    AsOfDateString = col1.replace('n','')
#                                    col1 = 'DTD'
#                                col2 = b1[1].strip()
#                                #print MySearchString,AsOfDateString,col1, col2
#                                mydict[len(mydict)] = {'source':'hfrx','product':MySearchString,'AsOfDate':AsOfDateString,'period':col1,'datavalue':col2,'filedatetime_string':filedatetime_string}
#                                
#    
                    
                
                #splitted = str(x).split('\\')
                #print splitted
        #import re
        #properties = soup.find_all('a', title=re.compile('%'))
        #for eachproperty in properties:
    #    print eachproperty['href']+",", eachproperty.string
        
except StopIteration:
  raise
except Exception as e:
  print(e) # or whatever kind of logging you want
  pass

        
for k,v in mydict.items():
    print k,v
## ###########################################################
## Enable this for production
#
#import csv
#with open(outputfile, 'wb') as f:  # Just use 'w' mode in 3.x
#    w = csv.DictWriter(f, mydict[0].keys(),delimiter = "|")
#    w.writeheader()
#    for k,v in mydict.items():
#        w.writerow(v)
#  
#copyFile(outputfile, uploadfile)
#     
#print 'you can find your file locally here:', outputfile
#print 'you can find your file on the sql server filesystem here:', uploadfile
## ###########################################################