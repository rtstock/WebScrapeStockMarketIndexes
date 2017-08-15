class perform:
    
    def __init__(self,
           # procname = 'xdeletethis_sylvan'
           # , params = {}
                     ):
        #print 'started good_readvalue_marketvalue_barclays_aggregate.py'
            a = 100

    def execute(self, numberofdaysback, localunprocessedpath = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\\Downloads\\Unprocessed\\barclays\\'):
        import datetime
        import os
        
        marketvalues_dict = {}
        today = datetime.date.today()
        print 'today is:', today

        dict_of_date8s = {}
        iref = numberofdaysback
        while True:
            #print 'iref',iref
            if iref > 0:
                break
            refdate = today + datetime.timedelta(days=iref)
            refdate8 = str(refdate).replace('-','')
            dict_of_date8s[len(dict_of_date8s)] = refdate8
            iref = iref + 1

        for key, value in sorted(dict_of_date8s.iteritems()):
            #print(key, value)

            #myfile = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\\Downloads\\Unprocessed\\barclays\\'+value+'.agg'
            
            myfile = os.path.join(localunprocessedpath,value + '.agg')
            #print myfile
            import os
            import good_readvalue_marketvalue_barclays_aggregate as o
            p = o.perform()
            mydict = p.execute(myfile)
            for k,v in mydict.items():
                #print k,v
                #print v
                date8 = os.path.basename(v['filename'])[:8]
                marketvalue = v['marketvalue']
                marketvalues_dict[date8] = marketvalue
        prevmv = -1
        returns_dict = {}
        for key, value in sorted(marketvalues_dict.iteritems()):
            currmv = float(value)
            #print(key, prevmv,currmv)
            if prevmv > 0:
                periodreturn = (currmv - prevmv) / prevmv
                returns_dict[key] = [prevmv,currmv,periodreturn]
            prevmv = currmv
            
        #for key, value in sorted(returns_dict.iteritems()):
        #    print key,value
            
        return returns_dict
        '''
        # ###############################
        # Create the csv file
        if len(mydict)>0:
            with open(outputfile, 'wb') as f:  # Just use 'w' mode in 3.x
                w = csv.DictWriter(f, mydict[0].keys(),delimiter = "|")
                w.writeheader()
                for k,v in mydict.items():
                    w.writerow(v)
            
            if os.path.exists(uploadfile):
                os.remove(uploadfile)
            shutil.move(outputfile, etluploadfolder)
        # ###############################
            print 'You can find your files here:',etluploadfolder
        else:
            print 'No files exist or all files were already processed'
        '''



if __name__ == "__main__":
    import sys
    try:
        o = perform()
        #o.readfile('C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\\Downloads\\Unprocessed\\barclays\\20170314.agg')
        mypath = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\\Downloads\\Unprocessed\\barclays\\'
        mydict = o.execute(-15,mypath)
        for key, value in sorted(mydict.iteritems()):
            print key,value
            
    except Exception as e:
        print(e)
        print 'this error occurred attempting to write to changethis.txt'
