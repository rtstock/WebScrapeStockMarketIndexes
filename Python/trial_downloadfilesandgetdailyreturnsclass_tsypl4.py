class perform:
    
    def __init__(self,
           # procname = 'xdeletethis_sylvan'
           # , params = {}
                     ):
        #print 'started good_readvalue_marketvalue_barclays_aggregate.py'
            a = 100

            
    def getdictofdate8sfromrefdate(self,myrefdate,PositiveNumberOfDaysBack):
        import datetime
        import os
        refdate = myrefdate
        print 'refdate is:', refdate
        dict_of_date8s = {}
        iref = PositiveNumberOfDaysBack * -1
        earliest_date = refdate + datetime.timedelta(days=iref)
        print 'earliest_date',earliest_date
        earliest_date8 = str(earliest_date).replace('-','')
        latest_date8 = earliest_date8
        while True:
            iref = iref + 1
            refdate = myrefdate + datetime.timedelta(days=iref)
            refdate8 = str(refdate).replace('-','')
            dict_of_date8s[len(dict_of_date8s)] = refdate8
            latest_date8 = refdate8
            if iref >= 0:
                break
        return dict_of_date8s


    def execute(self):
        df_monthly = self.get_treasury_oneyear_constant_maturity_history_monthly()
        
        print 'start print df_monthly'
        from calendar import monthrange
        import datetime

        lstfinal = []
        for index, row in df_monthly.iterrows():
            daysinmonth = monthrange(index.year, index.month)[1]
            ls1 = self.calcdaily(float(row["GS1"])+4.0,daysinmonth)
            refdate = datetime.date(index.year, index.month, daysinmonth)
            dictofdate8s = self.getdictofdate8sfromrefdate(refdate,daysinmonth)
            for k,v in dictofdate8s.items():
                dictcurr = {'date8':v,'dailyreturn':ls1[0] }
                lstfinal.append(dictcurr)
    
        print 'got here'
        ls_daily = self.get_treasury_oneyear_constant_maturity_history_daily()
        #print '----------------xx'
        #print ls_daily
        for dict_curr in ls_daily:
            lstfinal.append(dict_curr)

        for dictcurr in lstfinal:
            print dictcurr
        #path_to_download_folder = "\\\\ipcnet\\company\\misc\\Apl\\APL Benchmarks\\Data\\FRED Treasury downloads\\"
        #csv_filepath = path_to_download_folder +'One Year Constant Maturity (Monthly) ' + str(today_date) + '.csv'
        #df.to_csv(path_or_buf=csv_filepath, sep=',')

        return lstfinal

    def calcdaily(self,mtdreturn,numberofdays):
        #=(((F4/100)+1)^(1/E4)-1)*100
        import math
        lst = []
        for i in range(0,numberofdays):
            val = (((mtdreturn/100.0)+1.0)**(1.0/numberofdays)-1.0)*100.0
            roundedval = round(val,15)
            lst.append(roundedval)
        return lst
    def calcgeomean(self,list_of_returns):
        lst = []
        z = 1.0
        for d in list_of_returns:
            ret= d['averagedailyreturn']
            z = z*(1.0+(ret/100.0))
            #print 'z',z, len(list_of_returns)
        val = (z-1.0) * 100.0
        return val
        
        #print lst
        #from scipy import stats as scistats
        #return 1.0 - scistats.gmean(lst)


    def executeX(self,download_last_x_days = -30):    
        ########################################
        #download_last_x_days = -5
        ########################################
        if download_last_x_days >= 0:
            print 'the parameter download_last_x_days must be a negative number.'
        else:
            
            NumberOfDaysBack = -1 * download_last_x_days
            
            import sys
            print (sys.version)

            #url = 'https://www.hedgefundresearch.com/sites/default/files/index_data/hfrx_index_data.csv'
            url = 'https://www.hedgefundresearch.com/sites/default/files/index_data/hfrx_daily_index_data.csv'
            myindex = 'HFRXGI-D'

            import config
            import os
            outputpath =  config.localunprocessedfolder + '\\hfrx'
            sylvanready_daily_path = config.sylvanready_daily_path
            import datetime
            filedatetime = datetime.datetime.today()
            filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S%M')

            print filedatetime_string
            outputfile = outputpath + '\\hfrx monthly ' + filedatetime_string + '.csv'

            print 'pulling from www.hedgefundresearch.com ...'
            import requests
            import shutil
            user = 'justin.malinchak@ipcanswers.com'
            password = 'Flicker01'
            r = requests.get(url, auth=(user, password))
            print 'status_code',r.status_code
            print 'header',r.headers['content-type']
            print 'encoding',r.encoding
            #print r.text:

            import csv
            import requests
            import datetime
            d0 = datetime.datetime.today()
            min_date = d0

            f_values = []
            d_values = {}
            d_listofdicts = []
            with requests.Session() as s:
                download = s.get(url)

                decoded_content = download.content.decode('utf-8')

                cr = csv.reader(decoded_content.splitlines(), delimiter=',')
                my_list = list(cr)
                for row in my_list:
                    
                    if len(row) > 3:
                        
                        if row[2] == 'HFRXEH':
                            s_date = row[0]
                            d1 = datetime.datetime.strptime(s_date,"%m/%d/%Y")

                            delta = d0 - d1
                            if delta.days > NumberOfDaysBack:
                                break
                            s_pct = row[3]
                            f0_pct = s_pct.replace('%', '')
                            f0_date = d1.strftime('%Y%m%d')
                            if d1 < min_date:
                                min_date = d1
                                f0_date_min = f0_date
                            f_values.append([f0_date, f0_pct])
                            d_values[f0_date] = f0_pct
            dict_of_date8s = self.getdictofdate8s(-1*download_last_x_days)
            for k,v in sorted(dict_of_date8s.iteritems()):
                print 'dictofdate8s',k,v
                if v in d_values.keys():
                    dailyreturnvalue = d_values[v]
                else:
                    dailyreturnvalue = 0
                d_listofdicts.append({'date8':v,'dailyreturn':dailyreturnvalue})

            #for k,v in sorted(d_values.iteritems()):
            #    d_listofdicts.append({'date8':k,'dailyreturn':v})
            return d_listofdicts
    def get_treasury_oneyear_constant_maturity_history_monthly(self):
        import datetime
        today_date = datetime.date.today()
        from datetime import datetime
        from dateutil.relativedelta import relativedelta
        yearago_date = today_date + relativedelta(years=-1)
        monthnumber = -1*int(today_date.strftime('%m'))
        #print monthnumber
        yearago_date = yearago_date + relativedelta(months=-1)
        beginingofyear_date = today_date + relativedelta(months=monthnumber)
        #print today_date
        #print yearago_date
        import pandas_datareader.data as pdr
        result = pdr.DataReader("GS1", "fred", beginingofyear_date, today_date)
        print result
        return result


    def get_treasury_oneyear_constant_maturity_history_daily(self):
        print 'starting get_treasury_oneyear_constant_maturity_history_daily!!!'
        import datetime
        today_date = datetime.date.today()
        from dateutil.relativedelta import relativedelta
        startofmonth_date = today_date + relativedelta(days=-today_date.day+1)
        #startofmonth_date = today_date + relativedelta(days=-100)
        print 'startofmonth',startofmonth_date
        dictofdate8s = self.getdictofdate8sfromrefdate(today_date,today_date.day)
        
        
        import pandas_datareader.data as pdr
        df_dailyreturns = pdr.DataReader("DGS1", "fred", startofmonth_date, today_date)
        print df_dailyreturns
        print dictofdate8s

        ls_setup = []
        for k,date8 in dictofdate8s.items():
            datecompare = datetime.date(int(date8[:4]),int(date8[4:6]),int(date8[6:8]))
            
            if datecompare in df_dailyreturns.index:
                ls_setup.append([date8, float(df_dailyreturns.loc[datecompare]['DGS1'])])
            else:
                ls_setup.append([date8, 0.00])
        latest_non_zero_value = 0
        for item in ls_setup:
            if float(item[1]) != float(0.00):
                latest_non_zero_date_and_value = [item[0],float(item[1])]
                
        print 'latest_non_zero_date_and_value',latest_non_zero_date_and_value, latest_non_zero_date_and_value[0][6:]
        myyear = int(latest_non_zero_date_and_value[0][0:4])
        mymonth = int(latest_non_zero_date_and_value[0][4:6])
        daysinmonth =  int(latest_non_zero_date_and_value[0][6:])
        #y = 2/0
        ls1 = self.calcdaily(float(latest_non_zero_date_and_value[1]) + 4.00,int(latest_non_zero_date_and_value[0][6:]))
        
        refdate = datetime.date(myyear, mymonth, daysinmonth)
        dictofdate8s = self.getdictofdate8sfromrefdate(refdate,daysinmonth)
        lstfinal = []
        for k,v in dictofdate8s.items():
            dictcurr = {'date8':v,'dailyreturn':ls1[0] }
            #print dictcurr
            lstfinal.append(dictcurr)
        #FFFFFF
        #print lstfinal
        return lstfinal
    
    def get_treasury_oneyear_constant_maturity_history_daily_old(self):
        import datetime
        today_date = datetime.date.today()
        from datetime import datetime
        from dateutil.relativedelta import relativedelta
        #yearago_date = today_date + relativedelta(years=0)
        #yearago_date = yearago_date + relativedelta(months=-3)
        monthago_date = today_date + relativedelta(months=-1)
        #print today_date
        #print monthago_date

        import pandas_datareader.data as pdr
        result = pdr.DataReader("DGS1", "fred", monthago_date, today_date)
        return result

if __name__ == "__main__":
    import sys
    #try:
    if 1 == 1:
        import os
        import datetime
        o = perform()
        #refdate = datetime.date(2016, 8, 22)
        #print refdate
        #d8 = o.getdictofdate8sfromrefdate(refdate,10)
        #print d8
        listofdicts = o.execute()
        #for listitem in listofdicts:
        #    print listitem['date8'],listitem['dailyreturn']
