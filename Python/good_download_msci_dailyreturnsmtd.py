# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 10:50:44 2015

@author: justin.malinchak

------------
Description:
------------
    Downloads specific MSCI indexes for last day of each month going back [offsetmonths)]
    [offsetmonths] should be a negative number

"""

import datetime
from datetime import timedelta

# ==========
# Parameters
import config
outputpath =  config.localunprocessedfolder + '\\msci\\'

offsetmonths = 0

mydate = datetime.datetime.today()
offsetdays = mydate.day * -1
print offsetdays
#pause
#mydate = datetime.date(2012,7,5)
# ==========

#correctDate  = datetime.date(datetime.datetime.today().year,datetime.datetime.today().month,1) - timedelta(days=1)
#correctDate  = datetime.date(mydate.year,mydate.month,1) - timedelta(days=1)
#correctDate  = datetime.date(datetime.datetime.today().year,datetime.datetime.today().month,1) - timedelta(days=1)
correctDate  = datetime.date(mydate.year,mydate.month,mydate.day) + timedelta(days=1)
print('correctDate',str(correctDate))
#pause
import os
import urllib

lstCat =    [
            'DM Gross',
            'AC Gross',
            'EM Gross',
            'CM Gross',
            'DM Net',
            'AC Net',
            'DM Gross Value',
            'DM Net Value'
            ]


#import datetime
#from datetime import datetime

#enddate = datetime.date.today()
#enddate = correctDate #datetime.datetime.strptime('2015-05-28','%Y-%m-%d').date()


from dateutil.relativedelta import relativedelta

while offsetmonths <= 0:
    monthenddate = correctDate + relativedelta(months=offsetmonths)
    print 'monthenddate',monthenddate
    offsetmonths = offsetmonths + 1
    iteroffsetdays = offsetdays
    while iteroffsetdays <= 0:
        refdate = monthenddate + relativedelta(days = iteroffsetdays)   
        print 'pulling msci',refdate
        iteroffsetdays = iteroffsetdays + 1        
        refdate8 = str(refdate).replace('-','')
        month = refdate.strftime('%b')
        day = refdate.strftime('%d')
        year = refdate.strftime('%Y')

        for mycategory in lstCat:
            try:
                if mycategory == '':
                    url = 'https://Unknown'
                    print 'No Selection Group Entered'
                
                elif mycategory == 'DM Gross':  
                    # website - DM gross        Market:DM IndexLevel:Gross Size:Standard                        Example: MSCI THE WORLD INDEX	MSCIWD	3/31/2015	-1.50
                    url = 'https://app2.msci.com/webapp/indexperf/excel?scope=0&priceLevel=40&market=1897&style=C&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
                
                elif mycategory == 'AC Gross':
                    # website - AC gross        Unknown
                    url = 'https://app2.msci.com/webapp/indexperf/excel?scope=0&priceLevel=40&market=1896&style=C&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
                
                elif mycategory == 'EM Gross':
                    # website - EM gross        Market:EM IndexLevel:Gross Size:Standard                        Example: MSCI EMERGING MARKETS	MSCIEM	3/31/2015	-1.40
                    url = 'https://app2.msci.com/webapp/indexperf/excel?scope=0&priceLevel=40&market=1898&style=C&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
                
                elif mycategory == 'CM Gross': 
                    # website - CM gross        Market:CM IndexLevel:Gross Size:Standard                        Example: MSCI GOLDEN DRAGON	MSCIGD	3/31/2015	1.18
                    url = 'https://app2.msci.com/webapp/indexperf/excel?scope=0&priceLevel=40&market=2809&style=C&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
                    
                elif mycategory == 'DM Net': 
                    # website - DM net           Market:DM IndexLevel:Net Size:Standard                         Example: MSCI EAFE Net	EAFENT	3/31/2015	-1.52
                    url = 'https://app2.msci.com/webapp/indexperf/excel?scope=0&priceLevel=41&market=1897&style=C&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
                
                elif mycategory == 'AC Net': 
                    # website - AC net          Unknown                                                         Example: MSCI ALL COUNTRY WORLD INDEX NET	MSCIAN	3/31/2015	-1.55
                    url = 'https://app2.msci.com/webapp/indexperf/excel?scope=0&priceLevel=41&market=1896&style=C&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
                
                elif mycategory == 'DM Gross Value':
                    # website - DM gross value  Market:DM IndexLevel:Gross Size:StandardStyle:Value             Example: MSCI EAFE Value	EAFEV	3/31/2015	-1.89
                    url = 'https://app2.msci.com/webapp/indexperf/excel?scope=0&priceLevel=40&market=1897&style=V&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
                
                elif mycategory == 'DM Net Value':
                    # website - DM net value    Market:DM IndexLevel:Net Size:Standard Style:Value              Example: EAFE Value 3/31/2015 -1.89%
                    url = 'https://app2.msci.com/webapp/indexperf/excel?scope=0&priceLevel=41&market=1897&style=V&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'        
                #print refdate8,mycategory,url        
                local_path = os.path.join(outputpath,'msci '+refdate8+' '+mycategory.replace(' ','_')+'.xls')                
                if not 'Unknown' in url:
                    urllib.urlretrieve(url,local_path)
                    print '  ','complete:',local_path
                
            except StopIteration:
              raise
            except Exception as e:
              print(e) # or whatever kind of logging you want
              pass
