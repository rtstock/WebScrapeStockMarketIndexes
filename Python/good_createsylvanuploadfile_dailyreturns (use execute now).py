SuspendSendingViaFTP = False
import pandas as pd
import numpy as np
import config
import datetime
anchorday = datetime.date.today()

id_gp01 = 'SHLAGG-D'
import good_downloadandcalcproratedmtdreturnsclass_barclays_aggregate as f_gp01
o_gp01 = f_gp01.perform()
listofdicts_gp01 = o_gp01.execute(-5,anchorday)
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


id_gp02 = 'HFRXGI-D'
import good_downloadfilesandgetdailyreturnsclass_hfrx as f_gp02
o_gp02 = f_gp02.perform()
listofdicts_gp02 = o_gp02.execute(-30)
#for listitem_gp02 in listofdicts_gp02:
#    print 'gp02',listitem_gp02['date8'],listitem_gp02['dailyreturn']
df_gp02 = pd.DataFrame(listofdicts_gp02)
length_gp02 = len(df_gp02['date8'])
idarray_gp02 = np.repeat(id_gp02, length_gp02)
df_gp02['indexname']=idarray_gp02
df_gp02 = df_gp02.set_index('date8')
print df_gp02
myrow_gp02 = df_gp02.irow(0)
earliestdate8_gp02 = myrow_gp02.name
colname_gp02 = df_gp02.columns.values[0]
print 'earliestdate8_gp02',earliestdate8_gp02
print 'colname_gp02',colname_gp02

if 1 == 2:
    dummy = 1
else:
    f_final_1 = []
    #suppressed (Mike Cheng) f_final_1.append(['Record Type','Index Code','To Date'])
    f_final_1.append(['MID',id_gp01,earliestdate8_gp01])
    f_final_1.append(['MID',id_gp02,earliestdate8_gp02])

    f_final_2 = []
    for ir in df_gp01.itertuples():
        f_final_2.append(['MIH',id_gp01,ir[0],ir[0],'','','','','','','',''])
    for ir in df_gp02.itertuples():
        f_final_2.append(['MIH',id_gp02,ir[0],ir[0],'','','','','','','',''])

    f_final_3 = []
    for ir in df_gp01.itertuples():
        f_final_3.append(['MIV',id_gp01,id_gp01,ir[0],ir[0],'','','','','1',round(float(ir[1]),15),round(float(ir[1]),15)])
    for ir in df_gp02.itertuples():
        f_final_3.append(['MIV',id_gp02,id_gp02,ir[0],ir[0],'','','','','1',round(float(ir[1]),15),round(float(ir[1]),15)])
                          
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
        
        ftpreadyfilename = 'IDX_IPC_'+today.strftime('%Y%m%d')+'.csv'
        workingpath = config.watcheroutputpath
        import shutil
        srcfile = filelocation_string #os.path.join(config.sylvanready_daily_path,sylvanready_daily_filename) 
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
