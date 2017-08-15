# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 10:50:44 2015

@author: justin.malinchak
"""
import os
import urllib

outputpath = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\Downloads\\msci\\'

lstCat = ['DMgross',
'ACgross',
'EMgross',
'CMgross',
'DMnet',
'ACnet',
'DMgrossvalue',
'DMnetvalue']


import datetime
#from datetime import datetime

today = datetime.date.today()
print 'today is:', today

idate = -2

while True:
    refdate = today + datetime.timedelta(days=idate)
    refdate8 = str(refdate).replace('-','')
    #mydate = datetime.strptime(refdate8, '%Y%m%d')
    month = refdate.strftime('%b')
    day = refdate.strftime('%d')
    year = refdate.strftime('%Y')
    if idate > 0:
        break
    idate = idate + 1
    for mycategory in lstCat:

        try:
      
            if mycategory == '':
                url = 'https://Unknown'
                print 'No Selection Group Entered'
            
            elif mycategory == 'DMgross':  
                # website - DM gross        Market:DM IndexLevel:Gross Size:Standard                        Example: MSCI THE WORLD INDEX	MSCIWD	3/31/2015	-1.50
                url = 'https://app.msci.com/webapp/indexperf/excel?scope=0&priceLevel=40&market=1897&style=C&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
            
            elif mycategory == 'ACgross':
                # website - AC gross        Unknown
                url = 'https://app.msci.com/webapp/indexperf/excel?scope=0&priceLevel=40&market=1896&style=C&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
            
            elif mycategory == 'EMgross':
                # website - EM gross        Market:EM IndexLevel:Gross Size:Standard                        Example: MSCI EMERGING MARKETS	MSCIEM	3/31/2015	-1.40
                url = 'https://app.msci.com/webapp/indexperf/excel?scope=0&priceLevel=40&market=1898&style=C&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
            
            elif mycategory == 'CMgross': 
                # website - CM gross        Market:CM IndexLevel:Gross Size:Standard                        Example: MSCI GOLDEN DRAGON	MSCIGD	3/31/2015	1.18
                url = 'https://app.msci.com/webapp/indexperf/excel?scope=0&priceLevel=40&market=2809&style=C&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
                
            elif mycategory == 'DMnet': 
                # website - DM net           Market:DM IndexLevel:Net Size:Standard                         Example: MSCI EAFE Net	EAFENT	3/31/2015	-1.52
                url = 'https://app.msci.com/webapp/indexperf/excel?scope=0&priceLevel=41&market=1897&style=C&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
            
            elif mycategory == 'ACnet': 
                # website - AC net          Unknown                                                         Example: MSCI ALL COUNTRY WORLD INDEX NET	MSCIAN	3/31/2015	-1.55
                url = 'https://app.msci.com/webapp/indexperf/excel?scope=0&priceLevel=41&market=1896&style=C&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
            
            elif mycategory == 'DMgrossvalue':
                # website - DM gross value  Market:DM IndexLevel:Gross Size:StandardStyle:Value             Example: MSCI EAFE Value	EAFEV	3/31/2015	-1.89
                url = 'https://app.msci.com/webapp/indexperf/excel?scope=0&priceLevel=40&market=1897&style=V&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
            
            elif mycategory == 'DMnetvalue':
                # website - DM net value    Market:DM IndexLevel:Net Size:Standard Style:Value              Example: EAFE Value 3/31/2015 -1.89%
                url = 'https://app.msci.com/webapp/indexperf/excel?scope=0&priceLevel=41&market=1897&style=V&asOf='+month+'+'+day+'%2C+'+year+'&currency=15&size=36&export=Excel_IEIPerfRegional'
    
            print refdate8,mycategory,url
    
            local_path = os.path.join(outputpath,'msci '+refdate8+' '+mycategory+'.xls')
            
            if not 'Unknown' in url:
                urllib.urlretrieve(url,local_path)
                print '  ','complete:',local_path

        except StopIteration:
          raise
        except Exception as e:
          print(e) # or whatever kind of logging you want
          pass
