class perform:
    
    def __init__(self,
           # procname = 'xdeletethis_sylvan'
           # , params = {}
                     ):
        #print 'started good_readvalue_marketvalue_barclays_aggregate.py'
            a = 100
    def last_day_of_month(self,year, month):
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

    def getdictofmonthend8s(self,anchor_date,earliest_year):
        import os
        xfulldate = anchor_date.strftime('%Y-%m-%d %H.%M.%S')
        xmonth = int(anchor_date.strftime('%m'))
        xyear = int(anchor_date.strftime('%Y'))
        final_dict = {}
        while True:
            xmonth = xmonth - 1
            if xmonth == 0:
                xmonth = 12
                xyear = xyear - 1
            if xyear < earliest_year:
                break
            mylastday = self.last_day_of_month(xyear,xmonth)
            mylastday8 = str(mylastday).replace('-','')
            final_dict[mylastday8] = mylastday8
            #print 'mylastday', '=',mylastday
        return final_dict
    def getdictofdate8s(self,PositiveNumberOfDaysBack):
        import datetime
        import os
        today = datetime.date.today()
        print 'today is:', today
        dict_of_date8s = {}
        iref = PositiveNumberOfDaysBack * -1
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
        return dict_of_date8s

    def execute(self,earliest_year,sylvanid,hfrid):    
        ########################################
        #download_last_x_days = -5
        ########################################
        import datetime
        today = datetime.datetime.today()
        print 'today is:', today
        if 1 == 2:
            print 'the parameter download_last_x_days must be a negative number.'
        else:
            
            #NumberOfDaysBack = -1 * download_last_x_days
            
            import sys
            print (sys.version)

            url = 'https://www.hedgefundresearch.com/sites/default/files/index_data/hfrx_index_data.csv'
            #url = 'https://www.hedgefundresearch.com/sites/default/files/index_data/hfrx_daily_index_data.csv'
            myindex = sylvanid + '-D'

            import config
            import os
            outputpath =  config.localprocessedfolder + '\\hfrx'
            sylvanready_daily_path = config.sylvanready_daily_path
            import datetime
            filedatetime = datetime.datetime.today()
            filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S%M')

            print filedatetime_string
            outputfile = outputpath + '\\hfrx mtd ' + filedatetime_string + '.csv'
                
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
            d_listofdictsforprinting = []
            with requests.Session() as s:
                download = s.get(url)

                decoded_content = download.content.decode('utf-8')

                cr = csv.reader(decoded_content.splitlines(), delimiter=',')
                my_list = list(cr)
                for row in my_list:
                    
                    if len(row) > 3:
                        
                        if row[2] == hfrid:
                            s_date = row[0]
                            d1 = datetime.datetime.strptime(s_date,"%m/%d/%Y")

                            delta = d0 - d1

                            s_pct = row[3]
                            f0_pct = s_pct.replace('%', '')
                            f0_date = d1.strftime('%Y%m%d')
                            #print f0_date,f0_pct
                            if d1 < min_date:
                                min_date = d1
                                f0_date_min = f0_date
                            f_values.append([f0_date, f0_pct])
                            d_values[f0_date] = f0_pct
            #dict_of_date8s = self.getdictofdate8s(-1*download_last_x_days)
            dictofmonthend8s = self.getdictofmonthend8s(today,earliest_year)
            for k,v in sorted(dictofmonthend8s.iteritems()):
                #print 'dictofdate8s',k,v
                if v in d_values.keys():
                    mtdreturnvalue = d_values[v]
                else:
                    mtdreturnvalue = 0
                d_listofdicts.append({'date8':v,'mtdreturn':mtdreturnvalue})
                d_listofdictsforprinting.append({'date8':v,'measure':hfrid,'mtdreturn':mtdreturnvalue})
                
            #for k,v in sorted(d_values.iteritems()):
            #    d_listofdicts.append({'date8':k,'mtdreturn':v})
            print 'outputfile',outputfile
            import pandas as pd
            df = pd.DataFrame.from_records(d_listofdictsforprinting, index = None)
            with open(outputfile, 'w') as f:
                df.to_csv(f, header=True,index=False)
            

            
            return d_listofdicts
if __name__ == "__main__":
    import datetime
    today = datetime.datetime.today()
    print 'today is:', today

    import sys
    #try:
    if 1 == 1:
        import os
        o = perform()
        listofdicts = o.execute(2017,'HFRXGI','HFRXEH')
        #print listofdicts
        #rdict = o.getdictofmonthend8s(today,2010)
        for d in listofdicts:
            print d
        
