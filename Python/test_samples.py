# -*- coding: utf-8 -*-
"""
Created on Thu Jun 04 09:24:02 2015

@author: justin.malinchak
"""

# list comprehension
d = {}
nums = [1,2,3,4]
fruit = ["Apples", "Peaches", "Pears", "Bananas"]
d = [(i,f) for i in nums for f in fruit]
print d[4]
print '----'
# dictionary list comrehension
d1 = {chr(66+i) : i for i in range(6)}
print d1
print d1['E']
print '----'
print 'Iterables'
mylist = [x*x for x in range(3)]
for i in mylist:
    print(i)

print '----'
print 'generator'
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!

for i in mygenerator:
    print(i)

import datetime
print datetime.datetime.strptime('5/31/2015','%m/%d/%Y').date()
import sys
#sys.path.remove('c:\\Program Files\\Reference Assemblies\\Microsoft\\Framework\\v3.5\\')
#sys.path.append('c:\\Program Files\\Reference Assemblies\\Microsoft\\Framework\\v3.5')
print sys.path

#print sys.path

import datetime
filedatetime = datetime.datetime.today()
filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S%M')
print filedatetime_string

from datetime import timedelta
mydate = datetime.date(datetime.datetime.today().year,datetime.datetime.today().month,1) - timedelta(days=1)

from dateutil.relativedelta import relativedelta
refdate = mydate + relativedelta(months=-1)
print refdate

print 'A','hello.muni'[-4:]
print 'B','hello.muni'[:4]

ext = '.muni'
print 'C','hello.muni'[(-1)*(len(ext)-1):]
print 'D','hello.muni'[:4]

from dateutil.relativedelta import relativedelta
mydate = '2014-08'
mydate_asdate = datetime.datetime(int(mydate.split('-')[0]), int(mydate.split('-')[1]), 1)
mydate_eom = mydate_asdate+relativedelta(months=1,days=-1)
print mydate_eom

offsetmonths = 0
import datetime
from datetime import timedelta
correctDate  = datetime.date(datetime.datetime.today().year,datetime.datetime.today().month,1) - timedelta(days=1)
print(str(correctDate))

import sys
print sys.version_info

def CheckDate(DateString,DateFormat):
    import time
    date = DateString
    try:
      valid_date = time.strptime(date, DateFormat)
      print DateString,'is a valid date!'
      print valid_date
      return True
    except ValueError:
      print DateString,'is not a valid date'
      return False
print CheckDate('2014.1.1','%Y.%m.%d')


datacolumntitles = ['MTDTot','MktVal','Price']
for datacolumntitle in datacolumntitles:
    print datacolumntitle
    
def last_day_of_month(date):
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month+1, day=1) - datetime.timedelta(days=1)
    
calcLastDayOfMonth = last_day_of_month(datetime.date(2015, 5, 12))
print 'calcLastDayOfMonth',calcLastDayOfMonth
import datetime
year_asstring = calcLastDayOfMonth.strftime('%Y')
shortmonthname = calcLastDayOfMonth.strftime("%b") # 'dec'
destination_inputfilename = 'P:\\Apl\\APL Benchmarks\\Data\\' + year_asstring+'\\'+shortmonthname
print 'destination_inputfilename',destination_inputfilename
print 'Month as integer',int(calcLastDayOfMonth.strftime("%m")) # 'dec'
print 'Year as 2 char',(calcLastDayOfMonth.strftime("%Y"))[-2:] # 'dec'