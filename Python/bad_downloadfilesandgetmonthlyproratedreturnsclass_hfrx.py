SuspendSendingViaFTP = False
import pandas as pd
import numpy as np
import config

import datetime
today_date = datetime.date.today()
today_datetime = datetime.datetime.today()
print 'today is:', today_datetime

xfulldate = today_datetime.strftime('%Y-%m-%d %H.%M.%S')
xmonth = int(today_datetime.strftime('%m'))
xyear = int(today_datetime.strftime('%Y'))




id_gp03 = 'HFRXGI-D'
today_year = int(today_datetime.strftime('%Y'))
import good_readvalueclass_mtd_hfrx as rfile
o_gp03 = rfile.perform()
listofdicts_gp03 = o_gp03.execute(today_year)
df_gp03 = pd.DataFrame(listofdicts_gp03)
length_gp03 = len(df_gp03['date8'])
idarray_gp03 = np.repeat(id_gp03, length_gp03)
df_gp03['indexname'] = idarray_gp03
df_gp03 = df_gp03.set_index('date8')
print df_gp03
myrow_gp03 = df_gp03.irow(0)
earliestdate8_gp03 = myrow_gp03.name
colname_gp03 = df_gp03.columns.values[0]
print 'earliestdate8_gp03',earliestdate8_gp03
print 'colname_gp03',colname_gp03

