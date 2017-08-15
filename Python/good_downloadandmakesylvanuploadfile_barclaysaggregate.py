# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:12:41 2015

@author: justin.malinchak

Notes:
    Run this once per month to get the latest data from HFRX.
    Gets a file in Excel format
"""
#################################################################################
myindex = 'SHLAGG-D'
numberofdaysback = -2000
#################################################################################
import datetime
import os
import config
import json
d0 = datetime.datetime.today()
today = datetime.date.today()
earliest_date = today
print 'today is:', today
dict_of_date8s = {}
iref = numberofdaysback
while True:
    if iref > 0:
        break
    refdate = today + datetime.timedelta(days=iref)
    if refdate < earliest_date:
        earliest_date = refdate
    refdate8 = str(refdate).replace('-','')
    dict_of_date8s[len(dict_of_date8s)] = refdate8
    iref = iref + 1

earliest_date8 = str(earliest_date).replace('-','')
print earliest_date8
print '----------------------------------------------'

savedjsonfile = os.path.join(config.localdatafileoutputpath,'dailyreturns-barclays-usaggregate.json')

# open savedjsonfile into testing_dict, and print key values to screen
with open(savedjsonfile) as f:
    returns_dict = json.load(f)

if len(returns_dict) > 0:
    f_final_1 = []
    f_final_1.append(['Record Type','Index Code','To Date'])
    f_final_1.append(['MID',myindex,earliest_date8])

    f_final_2 = []
    f_final_2.append(['Record Type','Index Code','From Date','To Date','','','','','','','',''])
    for key, value in sorted(dict_of_date8s.iteritems()):
        #print value
        if value in returns_dict:
            this_dict = returns_dict[value]
            f_final_2.append(['MIH',myindex,this_dict['currdate'],this_dict['currdate'],'','','','','','','',''])
            
    f_final_3 = []    
    f_final_3.append(['Record Type','Index Code','Index Node Code','From Date','To Date','','','','','Weight','Return','Local Return'])
    for key, value in sorted(dict_of_date8s.iteritems()):
        #print value
        if value in returns_dict:
            this_dict = returns_dict[value]
            roundedreturn = round(this_dict['periodreturn']*100.0,2)
            f_final_3.append(['MIV',myindex,myindex,this_dict['currdate'],this_dict['currdate'],'','','','','1',roundedreturn,roundedreturn])
            print this_dict['currdate'],roundedreturn
    '''
    for item in f_final_1:
        print item
    for item in f_final_2:
        print item
    for item in f_final_3:
        print item
    ''' 
    import pandas as pd
                
    headers = f_final_1.pop(0)
    df_final_1 = pd.DataFrame(f_final_1,columns=headers)
    
    headers = f_final_2.pop(0)
    df_final_2 = pd.DataFrame(f_final_2,columns=headers)

    headers = f_final_3.pop(0)
    df_final_3 = pd.DataFrame(f_final_3,columns=headers)


    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #                                output to CSV
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    import os
    #filelocation_string = resolved_destination_pathfile #myoutputfolder + "\\intraday " + today_datestring + ' ' + symbol +'.csv'
    filelocation_string = 'P:\\Apl\\APL Benchmarks\\Data\\$Daily\\automated\\'+myindex+' '+ d0.strftime('%Y-%m-%d %H.%M.%S') + '.csv'
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

    '''     
if len(returns_dict) > 0:
    for key, value in sorted(dict_of_date8s.iteritems()):
        print value
        if value in returns_dict:
            print returns_dict[value]
    #for key, value in sorted(returns_dict.iteritems()):
    #    print value['currdate'], value['filedatetime'], value['periodreturn']

    f_final_1 = []
    f_final_1.append(['Record Type','Index Code','To Date'])
    f_final_1.append(['MID',myindex,f0_date_min])
    #for item in f_values:
    #    f_final_1.append(['MID',myindex,item[0]])

    f_final_2 = []
    f_final_2.append(['Record Type','Index Code','From Date','To Date','','','','','','','',''])
    for item in f_values:
        f_final_2.append(['MIH',myindex,item[0],item[0],'','','','','','','',''])

    f_final_3 = []    
    f_final_3.append(['Record Type','Index Code','Index Node Code','From Date','To Date','','','','','Weight','Return','Local Return'])
    for item in f_values:
        f_final_3.append(['MIV',myindex,myindex,item[0],item[0],'','','','','1',item[1],item[1]])
    f_final_3.append(['','','','','','','','','','','',''])
    
    for item in f_final_1:
        print item
    for item in f_final_2:
        print item
    for item in f_final_3:
        print item          

    
    import pandas as pd
                
    headers = f_final_1.pop(0)
    df_final_1 = pd.DataFrame(f_final_1,columns=headers)
    
    headers = f_final_2.pop(0)
    df_final_2 = pd.DataFrame(f_final_2,columns=headers)

    headers = f_final_3.pop(0)
    df_final_3 = pd.DataFrame(f_final_3,columns=headers)


    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #                                output to CSV
    #   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    import os
    #filelocation_string = resolved_destination_pathfile #myoutputfolder + "\\intraday " + today_datestring + ' ' + symbol +'.csv'
    filelocation_string = 'P:\\Apl\\APL Benchmarks\\Data\\$Daily\\automated\\'+myindex+' '+ d0.strftime('%Y-%m-%d %H.%M.%S') + '.csv'
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


'''
