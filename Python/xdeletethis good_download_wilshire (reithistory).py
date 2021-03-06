# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 10:50:44 2015

@author: justin.malinchak

------------
Description:
------------
    Downloads hfrx REIT index MTD returns for last day the previous month offset by [offsetmonths]

"""
import os
import urllib

# ==========
# Parameters
outputpath = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\Downloads\\Unprocessed\\hfrx\\'
url = 'https://www.hedgefundresearch.com/hfrx_reg/index.php'
offsetmonths = 0

import datetime
from datetime import timedelta
filedatetime = datetime.datetime.today()
filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S%M')
correctDate  = datetime.date(datetime.datetime.today().year,datetime.datetime.today().month,1) - timedelta(days=1)
correctDateString = str(correctDate).replace('-','')
print(str(correctDate))

#import datetime
#from datetime import datetime

#enddate = datetime.date.today()
#enddate = correctDate #datetime.datetime.strptime('2015-05-28','%Y-%m-%d').date()


from dateutil.relativedelta import relativedelta

while True:
    
    refdate = correctDate + relativedelta(months=offsetmonths)
    #refdate = enddate + datetime.timedelta(days=offsetmonths)
    refdate8 = str(refdate).replace('-','')
    #mydate = datetime.strptime(refdate8, '%Y%m%d')
    month = refdate.strftime('%b')
    day = refdate.strftime('%d')
    year = refdate.strftime('%Y')
    if offsetmonths > 0:
        break
    offsetmonths = offsetmonths + 1
    #for mycategory in lstCat:
    
    try:
  
        # website - DM gross        Market:DM IndexLevel:Gross Size:Standard                        Example: hfrx THE WORLD INDEX	hfrxWD	3/31/2015	-1.50
        #url = 'https://app.hfrx.com/webapp/indexperf/excel?scope=0&priceLevel=40&market=1897&style=C&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
        
        #url = 'http://www.hfrx.com/indexcalculator/IndexCalculator/api/index/cumulative/302/1/'+correctDateString+'/1?_dc=1433956529495'
        #correctDateString

        local_path = os.path.join(outputpath,'hfrx '+refdate8+' '+ filedatetime_string +'.php')
        
        if not 'Unknown' in url:
            urllib.urlretrieve(url,local_path)
            
            print '  ','complete:',local_path

    except StopIteration:
      raise
    except Exception as e:
      print(e) # or whatever kind of logging you want
      pass
