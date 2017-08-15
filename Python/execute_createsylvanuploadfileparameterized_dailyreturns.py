SuspendSendingViaFTP = False
import pandas as pd
import numpy as np
import config

import datetime
today_date = datetime.date.today()
today_datetime = datetime.datetime.today()
print 'today is:', today_datetime

xfulldate = today_datetime.strftime('%Y-%m-%d %H.%M.%S')
xday = int(today_datetime.strftime('%d'))
xmonth = int(today_datetime.strftime('%m'))
xyear = int(today_datetime.strftime('%Y'))

from datetime import timedelta 
 
def subtract_one_month(dt0): 
    dt1 = dt0.replace(days=1) 
    dt2 = dt1 - timedelta(days=1) 
    dt3 = dt2.replace(days=1) 
    return dt3

def last_day_of_month(year, month):
    from datetime import datetime
    """ Work out the last day of the month """
    last_days = [31, 30, 29, 28, 27]
    for i in last_days:
        try:
            end = datetime(year, month, i)
        except ValueError:
            continue
        else:
            return end.date()
    return None
from datetime import datetime
from dateutil.relativedelta import relativedelta

date_previous_month = today_datetime + relativedelta(months=-1)
last_day_previous_month = last_day_of_month(date_previous_month.year,date_previous_month.month)

id_gp00 = 'SHLAGG-D'
import good_downloadandcalcproratedmtdreturnsclass_barclays_aggregate as f_gp00
o_gp00 = f_gp00.perform()
listofdicts_gp00 = o_gp00.execute(-5,last_day_previous_month)
#for listitem_gp00 in listofdicts_gp00:
#    print 'gp00',listitem_gp00['date8'],listitem_gp00['averagedailyreturn']
df_gp00 = pd.DataFrame(listofdicts_gp00)
print 'length ######',len(df_gp00)
if not len(df_gp00) > 0:
    print 'nothing found for SHLAGG-D (-5,'+str(last_day_previous_month)+')'

    earliestdate8_gp00 = ''
else:
    length_gp00 = len(df_gp00['date8'])
    idarray_gp00 = np.repeat(id_gp00, length_gp00)
    df_gp00['indexname']=idarray_gp00
    df_gp00 = df_gp00.set_index('date8')
    myrow_gp00 = df_gp00.irow(0)
    earliestdate8_gp00 = myrow_gp00.name
    colname_gp00 = df_gp00.columns.values[0]
    print df_gp00
    print 'earliestdate8_gp00',earliestdate8_gp00
    print 'colname_gp00',colname_gp00


id_gp01 = 'SHLAGG-D'
import good_downloadandcalcproratedmtdreturnsclass_barclays_aggregate as f_gp01
o_gp01 = f_gp01.perform()
listofdicts_gp01 = o_gp01.execute(-5,today_date)
#for listitem_gp01 in listofdicts_gp01:
#    print 'gp01',listitem_gp01['date8'],listitem_gp01['averagedailyreturn']
df_gp01 = pd.DataFrame(listofdicts_gp01)
length_gp01 = len(df_gp01['date8'])
idarray_gp01 = np.repeat(id_gp01, length_gp01)
df_gp01['indexname']=idarray_gp01
df_gp01 = df_gp01.set_index('date8')
myrow_gp01 = df_gp01.irow(0)
earliestdate8_gp01 = myrow_gp01.name
colname_gp01 = df_gp01.columns.values[0]
print df_gp01
print 'earliestdate8_gp01',earliestdate8_gp01
print 'colname_gp01',colname_gp01

# Gets prorated daily returns from beginning of year to end of last month
id_gp02 = 'HFRXGI-D'
earliestdate8_gp02 = '99999999'
df_gp02 = pd.DataFrame() 
today_year = int(today_datetime.strftime('%Y'))
import good_readvalueclass_mtd_parameterized_hfrx as rfile
o_gp02 = rfile.perform()
listofdicts_gp02 = o_gp02.execute(today_year,'HFRXGI','HFRXEH')
if 1 == 1:
    if len(listofdicts_gp02) > 0:
        df_gp02 = pd.DataFrame(listofdicts_gp02)
        length_gp02 = len(df_gp02['date8'])
        idarray_gp02 = np.repeat(id_gp02, length_gp02)
        df_gp02['indexname'] = idarray_gp02
        df_gp02 = df_gp02.set_index('date8')
        print df_gp02
        myrow_gp02 = df_gp02.irow(0)
        earliestdate8_gp02 = myrow_gp02.name
        colname_gp02 = df_gp02.columns.values[0]
        print 'earliestdate8_gp02',earliestdate8_gp02
        print 'colname_gp02',colname_gp02

# Gets actual daily returns from beginning of current month to now
id_gp03 = 'HFRXGI-D'
import good_downloadfilesandgetdailyreturnsclassparameterized_hfrx as f_gp03
o_gp03 = f_gp03.perform()
listofdicts_gp03 = o_gp03.execute(-1*(int(xday)-1),'HFRXGI','HFRXEH')
#for listitem_gp03 in listofdicts_gp03:
#    print 'gp03',listitem_gp03['date8'],listitem_gp03['dailyreturn']
df_gp03 = pd.DataFrame(listofdicts_gp03)
length_gp03 = len(df_gp03['date8'])
idarray_gp03 = np.repeat(id_gp03, length_gp03)
df_gp03['indexname']=idarray_gp03
df_gp03 = df_gp03.set_index('date8')
print df_gp03
myrow_gp03 = df_gp03.irow(0)
earliestdate8_gp03 = myrow_gp03.name
colname_gp03 = df_gp03.columns.values[0]
print 'earliestdate8_gp03',earliestdate8_gp03
print 'colname_gp03',colname_gp03

# Gets actual daily returns from beginning of current month to now
id_gp04 = 'TSYPL4-D'
import good_downloadfilesandgetdailyreturnsclass_tsypl4 as f_gp04
o_gp04 = f_gp04.perform()
listofdicts_gp04 = o_gp04.execute()
#for listitem_gp04 in listofdicts_gp04:
#    print 'gp04',listitem_gp04['date8'],listitem_gp04['dailyreturn']
df_gp04 = pd.DataFrame(listofdicts_gp04)
length_gp04 = len(df_gp04['date8'])
idarray_gp04 = np.repeat(id_gp04, length_gp04)
df_gp04['indexname']=idarray_gp04
df_gp04 = df_gp04.set_index('date8')
print df_gp04
myrow_gp04 = df_gp04.irow(0)
earliestdate8_gp04 = myrow_gp04.name
colname_gp04 = df_gp04.columns.values[0]
print 'earliestdate8_gp04',earliestdate8_gp04
print 'colname_gp04',colname_gp04

# Gets prorated daily returns from beginning of year to end of last month
#good_downloadfilesandgetdailyreturnsclassparameterized_hfrx.py
id_gp05 = 'HFRXGH-D'
earliestdate8_gp05 = '99999999'
df_gp05 = pd.DataFrame() 
today_year = int(today_datetime.strftime('%Y'))
import good_readvalueclass_mtd_parameterized_hfrx as rfile
o_gp05 = rfile.perform()
listofdicts_gp05 = o_gp05.execute(today_year,'HFRXGH','HFRXGL')
print 'listofdicts_gp05',len(listofdicts_gp05),'uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'
if 1 == 1:
    if len(listofdicts_gp05) > 0:
        df_gp05 = pd.DataFrame(listofdicts_gp05)
        length_gp05 = len(df_gp05['date8'])
        idarray_gp05 = np.repeat(id_gp05, length_gp05)
        df_gp05['indexname'] = idarray_gp05
        df_gp05 = df_gp05.set_index('date8')
        print df_gp05
        myrow_gp05 = df_gp05.irow(0)
        earliestdate8_gp05 = myrow_gp05.name
        colname_gp05 = df_gp05.columns.values[0]
        print 'earliestdate8_gp05',earliestdate8_gp05
        print 'colname_gp05',colname_gp05

# Gets actual daily returns from beginning of current month to now
id_gp06 = 'HFRXGH-D'
import good_downloadfilesandgetdailyreturnsclassparameterized_hfrx as f_gp06
o_gp06 = f_gp06.perform()
listofdicts_gp06 = o_gp06.execute(-1*(int(xday)-1),'HFRXGH','HFRXGL')
#for listitem_gp06 in listofdicts_gp06:
#    print 'gp06',listitem_gp06['date8'],listitem_gp06['dailyreturn']
df_gp06 = pd.DataFrame(listofdicts_gp06)
length_gp06 = len(df_gp06['date8'])
idarray_gp06 = np.repeat(id_gp06, length_gp06)
df_gp06['indexname']=idarray_gp06
df_gp06 = df_gp06.set_index('date8')
print df_gp06
myrow_gp06 = df_gp06.irow(0)
earliestdate8_gp06 = myrow_gp06.name
colname_gp06 = df_gp06.columns.values[0]
print 'earliestdate8_gp06',earliestdate8_gp06
print 'colname_gp06',colname_gp06



if 1 == 2:
    dummy = 1
else:
    f_final_1 = []
    if not str(earliestdate8_gp00) == '':
        f_final_1.append(['MID',id_gp01,earliestdate8_gp00])
    if earliestdate8_gp03 < earliestdate8_gp02:
        f_final_1.append(['MID',id_gp03,earliestdate8_gp03])
    else:
        f_final_1.append(['MID',id_gp03,earliestdate8_gp02])
    f_final_1.append(['MID',id_gp04,earliestdate8_gp04])
    if earliestdate8_gp06 < earliestdate8_gp05:
        f_final_1.append(['MID',id_gp06,earliestdate8_gp06])
    else:
        f_final_1.append(['MID',id_gp05,earliestdate8_gp05])
    
    f_final_2 = []
    for ir in df_gp00.itertuples():
        f_final_2.append(['MIH',id_gp00,ir[0],ir[0],'','','','','','','',''])
    for ir in df_gp01.itertuples():
        f_final_2.append(['MIH',id_gp01,ir[0],ir[0],'','','','','','','',''])
    for ir in df_gp02.itertuples():
        f_final_2.append(['MIH',id_gp02,ir[0],ir[0],'','','','','','','',''])
    for ir in df_gp03.itertuples():
        f_final_2.append(['MIH',id_gp03,ir[0],ir[0],'','','','','','','',''])
    for ir in df_gp04.itertuples():
        f_final_2.append(['MIH',id_gp04,ir[0],ir[0],'','','','','','','',''])
    for ir in df_gp05.itertuples():
        f_final_2.append(['MIH',id_gp05,ir[0],ir[0],'','','','','','','',''])
    for ir in df_gp06.itertuples():
        f_final_2.append(['MIH',id_gp06,ir[0],ir[0],'','','','','','','',''])
        
    f_final_3 = []
    for ir in df_gp00.itertuples():
        roundedvalue = round(float(ir[1]),15)
        f_final_3.append(['MIV',id_gp00,id_gp00,ir[0],ir[0],'','','','','1',roundedvalue,roundedvalue])

    for ir in df_gp01.itertuples():
        roundedvalue = round(float(ir[1]),15)
        f_final_3.append(['MIV',id_gp01,id_gp01,ir[0],ir[0],'','','','','1',roundedvalue,roundedvalue])

    for ir in df_gp02.itertuples():
        roundedvalue = round(float(ir[1]),15)
        f_final_3.append(['MIV',id_gp02,id_gp02,ir[0],ir[0],'','','','','1',roundedvalue,roundedvalue])

    for ir in df_gp03.itertuples():
        roundedvalue = round(float(ir[1]),15)
        f_final_3.append(['MIV',id_gp03,id_gp03,ir[0],ir[0],'','','','','1',roundedvalue,roundedvalue])

    for ir in df_gp04.itertuples():
        roundedvalue = round(float(ir[1]),15)
        f_final_3.append(['MIV',id_gp04,id_gp04,ir[0],ir[0],'','','','','1',roundedvalue,roundedvalue])

    for ir in df_gp05.itertuples():
        roundedvalue = round(float(ir[1]),15)
        f_final_3.append(['MIV',id_gp05,id_gp05,ir[0],ir[0],'','','','','1',roundedvalue,roundedvalue])

    for ir in df_gp06.itertuples():
        roundedvalue = round(float(ir[1]),15)
        f_final_3.append(['MIV',id_gp06,id_gp06,ir[0],ir[0],'','','','','1',roundedvalue,roundedvalue])
                          
    for item in f_final_1:
        print item
    for item in f_final_2:
        print item
    for item in f_final_3:
        print item
                            
    headers = f_final_1.pop(0)
    df_final_1 = pd.DataFrame(f_final_1,columns=headers)

    headers = f_final_2.pop(0)
    df_final_2 = pd.DataFrame(f_final_2,columns=headers)

    headers = f_final_3.pop(0)
    df_final_3 = pd.DataFrame(f_final_3,columns=headers)

    '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                    output to CSV
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
    
    #filelocation_string = resolved_destination_pathfile #myoutputfolder + "\\intraday " + today_datestring + ' ' + symbol +'.csv'
    
    #filelocation_string = 'P:\\Apl\\APL Benchmarks\\Data\\$Daily\\automated\\'+myindex+' '+ d0.strftime('%Y-%m-%d %H.%M.%S') + '.csv'
    import datetime
    import os
                    
    today_datetime = datetime.datetime.today()
    print 'today is:', today_datetime

    today_date8 = str(today_datetime).replace('-','')
            
    sylvanready_daily_filename = 'IPC '+ today_datetime.strftime('%Y-%m-%d %H.%M.%S') + '.csv'
    filelocation_string = os.path.join(config.sylvanready_daily_path,sylvanready_daily_filename)
    
    if os.path.isfile(filelocation_string) == True:
        os.remove(filelocation_string)
    if os.path.isfile(filelocation_string) == True:
        print 'Could not delete file',filelocation_string
    else:
        print 'Attempting to create filelocation_string',filelocation_string
        with open(filelocation_string, 'w') as f:
            df_final_1.to_csv(f, header=True,index=False)
        with open(filelocation_string, 'a') as f:
            df_final_2.to_csv(f, header=True,index=False)
        with open(filelocation_string, 'a') as f:
            df_final_3.to_csv(f, header=True,index=False)

    print 'You can find your file here',filelocation_string   

    if SuspendSendingViaFTP == True:
        print 'The FTP process was suspended.'
    else:
        ##    ## ##########################################################
        ##    ## Send file via ftp


        import ftplib
        import os
        todaysdate8 = str(today_date).replace('-','')
    
        pathtofile = config.sylvanready_daily_path
        ftpreadyfilename = 'IDX_IPC_'+today_date.strftime('%Y%m%d')+'.csv'
        workingpath = config.watcheroutputpath
        import shutil
        srcfile = os.path.join(config.sylvanready_daily_path,sylvanready_daily_filename) 
        dstfile = os.path.join(workingpath,ftpreadyfilename)
        print dstfile
        shutil.copy(srcfile,dstfile)

        import ftplib
        from ftplib import FTP 
        import os
        File2Send = dstfile
        if os.path.exists(File2Send):
            print 'found file'
        Output_Directory = "//usr//ssc519//SSIS//Index"

        ftp = FTP("ftp.sscgateway.com")
        ftp.login('ssc519', 'G2343DRTA') 

        file = open(File2Send, "rb")

        ftp.cwd(Output_Directory)

        ftp.storbinary('STOR ' + os.path.basename(File2Send), file) 

        ftp.quit() 
        file.close() 
        print "File transfered via FTP to","ftp.sscgateway.com",Output_Directory+'//'+ftpreadyfilename
