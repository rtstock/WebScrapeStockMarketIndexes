# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:28:10 2015

@author: Justin.Malinchak
"""

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


# ==========
# Parameters
outputpath = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\Downloads\\Unprocessed\\msci\\'
offsetmonths = -3
offsetdays= -3

import datetime
from datetime import timedelta

mydate = datetime.datetime.today()
mydate = datetime.date(2011,5,5)
#correctDate  = datetime.date(datetime.datetime.today().year,datetime.datetime.today().month,1) - timedelta(days=1)
correctDate  = datetime.date(mydate.year,mydate.month,1) - timedelta(days=1)
print(str(correctDate))

from dateutil.relativedelta import relativedelta

while offsetmonths <= 0:
    refdate = correctDate + relativedelta(months=offsetmonths)
    offsetdays = -3
    while offsetdays <= 0:
        #refdate = enddate + datetime.timedelta(days=offsetmonths)
        iterdate = refdate + relativedelta(days = offsetdays)        
        print 'iterdate',iterdate
        offsetdays = offsetdays + 1
    offsetmonths = offsetmonths + 1