
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
###########################################
SuspendSendingViaFTP = True
id_gp00 = 'SHLAGG-D'
earliest_year = 2011
downloadfiles = False
###########################################

import datetime
import os

today = datetime.datetime.today()
print 'today is:', today

xfulldate = today.strftime('%Y-%m-%d %H.%M.%S')
xmonth = int(today.strftime('%m'))
xyear = int(today.strftime('%Y'))

import good_downloadandcalcproratedmtdreturnsclass_barclays_aggregate
import good_calcproratedmtdreturnsclass_barclays_aggregate

print '@@@@@@@@@@@@@@@@@@',xyear,xmonth
listofdicts_gpXX = []

while True:
    xmonth = xmonth - 1
    if xmonth == 0:
        xmonth = 12
        xyear = xyear - 1
    if xyear < earliest_year:
        break
    mylastday = last_day_of_month(xyear,xmonth)
    print 'mylastday', '=',mylastday
    if downloadfiles == True:
        o1 = good_downloadandcalcproratedmtdreturnsclass_barclays_aggregate.perform()
    else:
        o1 = good_calcproratedmtdreturnsclass_barclays_aggregate.perform()
        
    listofdicts1 = o1.execute(-5,mylastday)
    
    if len(listofdicts1) > 0:
        print 'OK returns found for',mylastday
        #for item in listofdicts1:
        #    print item
    else:
        print 'NO returns for',mylastday
    listofdicts_gpXX.extend(listofdicts1)
    
earliestdate8_gp00 = '99999999'
dictofdicts_gp00 = {}
for item in listofdicts_gpXX:
    dictofdicts_gp00[item['date8']]= item    
    if item['date8'] < earliestdate8_gp00:
        earliestdate8_gp00 = item['date8']

listofdicts_gp00 = []
for k in sorted(dictofdicts_gp00):
    listofdicts_gp00.extend(dictofdicts_gp00[k])
print listofdicts_gp00
import pandas as pd
df_gp00 = pd.DataFrame(listofdicts_gp00)
print df_gp00
df_gp00 = df_gp00.set_index('date8')
## #######################################################################################

if 1 == 2:
    dummy = 1
else:
    f_final_1 = []
    #suppressed (Mike Cheng) f_final_1.append(['Record Type','Index Code','To Date'])
    f_final_1.append(['MID',id_gp00,earliestdate8_gp00])
    #f_final_1.append(['MID',id_gp02,earliestdate8_gp02])

    f_final_2 = []
    for ir in df_gp00.itertuples():
        f_final_2.append(['MIH',id_gp00,ir[0],ir[0],'','','','','','','',''])
    #for ir in df_gp02.itertuples():
    #    f_final_2.append(['MIH',id_gp02,ir[0],ir[0],'','','','','','','',''])

    f_final_3 = []
    for ir in df_gp00.itertuples():
        roundedvalue = round(float(ir[1]),15)
        f_final_3.append(['MIV',id_gp00,id_gp00,ir[0],ir[0],'','','','','1',roundedvalue,roundedvalue])
    #for ir in df_gp02.itertuples():
    #    f_final_3.append(['MIV',id_gp02,id_gp02,ir[0],ir[0],'','','','','1',ir[1],ir[1]])
                          
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
    import config      
    today = datetime.datetime.today()
    print 'today is:', today

    today_date8 = str(today).replace('-','')
            
    sylvanready_daily_filename = 'IPC '+ today.strftime('%Y-%m-%d %H.%M.%S') + '.csv'
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
        todaysdate8 = x
        pathtofile = sylvanready_daily_path
        ftpreadyfilename = 'IDX_IPC_'+today.strftime('%Y%m%d')+'.csv'
        workingpath = config.watcheroutputpath
        import shutil
        srcfile = os.path.join(sylvanready_daily_path,sylvanready_daily_filename) 
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

