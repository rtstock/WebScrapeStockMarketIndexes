class perform:
    
    def __init__(self,
           # procname = 'xdeletethis_sylvan'
           # , params = {}
                     ):
        #print 'started good_readvalue_marketvalue_barclays_aggregate.py'
            a = 100
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

    def execute(self,download_last_x_days = -30):    
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
if __name__ == "__main__":
    import sys
    #try:
    if 1 == 1:
        import os
        o = perform()
        listofdicts = o.execute(-30)
        for listitem in listofdicts:
            print listitem['date8'],listitem['dailyreturn']
