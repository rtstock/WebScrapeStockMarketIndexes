class perform:
    
    def __init__(self,
           # procname = 'xdeletethis_sylvan'
           # , params = {}
                     ):
        #print 'started good_readvalue_marketvalue_barclays_aggregate.py'
            a = 100
    def execute(self,download_last_x_days = -5):    
        ########################################
        #download_last_x_days = -5
        ########################################
        if download_last_x_days >= 0:
            print 'the parameter download_last_x_days must be a negative number.'
        else:
            import good_downloadclass_barclays_specifyindex as f1
            cls1 = f1.perform()
            pathtofiles = cls1.execute(download_last_x_days,'.agg')
            print pathtofiles

            import datetime
            today = datetime.date.today()
            print 'today is:', today
            dict_of_date8s = {}
            iref = download_last_x_days
            while True:
                if iref > 0:
                    break
                refdate = today + datetime.timedelta(days=iref)
                refdate8 = str(refdate).replace('-','')
                dict_of_date8s[len(dict_of_date8s)] = refdate8
                iref = iref + 1
            import os
            latestfilepathname = ''
            for k,refdate8 in sorted(dict_of_date8s.iteritems()):
                filepathname = os.path.join(pathtofiles,refdate8+'.agg')
                if os.path.exists(filepathname):
                    fileinfo = os.stat(filepathname)
                    filesize = fileinfo.st_size
                    if filesize > 0:
                        latestfilepathname = filepathname
            print 'latestfilepathname',latestfilepathname
            import good_readvalueclass_mtd_barclays_aggregate as cls2
            o = cls2.perform()
            listofdicts = o.execute(latestfilepathname)
            return listofdicts
        
            #print listofdicts
            #for listitem in listofdicts:
            #    print listitem['date8'],listitem['averagedailyreturn']
            ########################################################################
            ### save updated_dict to savedjsonfile
            ### Get path of savedjsonfile
            ##import config
            ##savedjsonfile = os.path.join(config.localdatafileoutputpath,'proratedmtcreturns-barclays-usaggregate.json')
            ##
            ##import json
            ##with open(savedjsonfile, 'w') as f:
            ##    json.dump(listofdicts, f)
            ##
            ##print 'you can find you file here ',savedjsonfile
            ########################################################################

if __name__ == "__main__":
    import sys
    #try:
    if 1 == 1:
        import os
        o = perform()
        resultlistofdicts = o.execute(-5)
        print resultlistofdicts
