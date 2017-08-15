###################
# hold this for later, it creates the sylvan upload file


            #######################################################################
            #import csv

            filepath = os.path.join(sylvanready_daily_path,myindex+' '+ d0.strftime('%Y-%m-%d %H.%M.%S') + '.csv')

            #with open(filepath,'wb') as resultFile:
            #    wr = csv.writer(resultFile, quoting=csv.QUOTE_NONE, escapechar="\"", quotechar="\\")
            #    for row in f_final:
            #        #s1 = str(row).replace('"','')
            #        wr.writerow([row])

            import datetime
            import os
                    
            today = datetime.date.today()
            print 'today is:', today
            dict_of_date8s = {}
            iref = NumberOfDaysBack * -1
            earliest_date = today + datetime.timedelta(days=iref)
            earliest_date8 = str(earliest_date).replace('-','')
            latest_date8 = earliest_date8
            while True:
                if iref >= 0:
                    break
                refdate = today + datetime.timedelta(days=iref)
                refdate8 = str(refdate).replace('-','')
                dict_of_date8s[len(dict_of_date8s)] = refdate8
                latest_date8 = refdate8
                iref = iref + 1

            status = 'started ' + str(today)
            print status

            if len(f_values) == 0:
                status = status + chr(10) + 'no data from www.hedgefundresearch.com was downloaded'

            else:
                f_final_1 = []
                #suppressed (Mike Cheng) f_final_1.append(['Record Type','Index Code','To Date'])
                f_final_1.append(['MID',myindex,earliest_date8])
                #for item in f_values:
                #    f_final_1.append(['MID',myindex,item[0]])

                f_final_2 = []
                #suppressed (Mike Cheng) f_final_2.append(['Record Type','Index Code','From Date','To Date','','','','','','','',''])
                for k,date8 in dict_of_date8s.items():
                    f_final_2.append(['MIH',myindex,date8,date8,'','','','','','','',''])

                f_final_3 = []    
                #suppressed (Mike Cheng) f_final_3.append(['Record Type','Index Code','Index Node Code','From Date','To Date','','','','','Weight','Return','Local Return'])
                for k,date8 in dict_of_date8s.items():
                    if date8 in d_values.keys():
                        f_final_3.append(['MIV',myindex,myindex,date8,date8,'','','','','1',d_values[date8],d_values[date8]])
                    else:
                        f_final_3.append(['MIV',myindex,myindex,date8,date8,'','','','','1',0,0])
                #suppressed (Mike Cheng) f_final_3.append(['','','','','','','','','','','',''])
                
            ##    for item in f_final_1:
            ##        print item
            ##    for item in f_final_2:
            ##        print item
            ##    for item in f_final_3:
            ##        print item          

                import pandas as pd
                            
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
                sylvanready_daily_filename = myindex+' '+ d0.strftime('%Y-%m-%d %H.%M.%S') + '.csv'
                filelocation_string = os.path.join(sylvanready_daily_path,sylvanready_daily_filename)
                
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
                    pathtofile = sylvanready_daily_path
                    ftpreadyfilename = 'IDX_IPC_'+latest_date8+'.csv'
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
