class perform:
    
    def __init__(self,
           # procname = 'xdeletethis_sylvan'
           # , params = {}
                     ):
        #print 'started good_readvalue_marketvalue_barclays_aggregate.py'
            a = 100
    def execute(self,earliest_year):
        import os
        import datetime
        #d = self.getrawreturnvaluedict(localunprocessedcsvpathname)
        #print d
        import good_downloadfilesandgetmtdreturnsclass_hfrx
        o1 = good_downloadfilesandgetmtdreturnsclass_hfrx.perform()
        listofdicts1 = o1.execute(earliest_year)
        for currdict in listofdicts1:
            currdate = datetime.datetime.strptime(currdict['date8'],"%Y%m%d")
            dayofmonth = int(currdate.strftime("%d"))
            mtdreturn = float(currdict['mtdreturn'])
            
            lstx = self.calcdaily(mtdreturn,dayofmonth)
            dictofdate8s = self.getdate8dictionary(currdict['date8'],dayofmonth)
            resultlst = []
            for k,d8 in dictofdate8s.items():
                resultlst.append({'date8':d8,'averagedailyreturn':lstx[k]})
                print currdict['date8'], currdict['mtdreturn'],dayofmonth,d8,lstx[k]
            mygeomean = self.calcgeomean(resultlst)

        print 'calculated geomean',mygeomean, 'should equal the provided',mtdreturn, 'parameter'
        return resultlst
    def getdate8dictionary(self,FromDate8,NumberOfDaysBack):
        import datetime
        import os
        startdate = datetime.datetime.strptime(FromDate8, "%Y%m%d")
        
        print 'startdate is:', startdate
        dict_of_date8s = {}
        iref = NumberOfDaysBack * -1
        earliest_date = startdate + datetime.timedelta(days=iref)
        earliest_date8 = str(earliest_date).replace('-','')
        latest_date8 = earliest_date8
        while True:
            if iref >= 0:
                break
            refdate = startdate + datetime.timedelta(days=iref+1)
            refdate8 = str(refdate).replace('-','').split(' ')[0]
            dict_of_date8s[len(dict_of_date8s)] = refdate8
            latest_date8 = refdate8
            iref = iref + 1
        return dict_of_date8s
    def calcdaily(self,mtdreturn,numberofdays):
        #=(((F4/100)+1)^(1/E4)-1)*100
        import math
        lst = []
        for i in range(0,numberofdays):
            val = (((mtdreturn/100.0)+1.0)**(1.0/numberofdays)-1.0)*100.0
            lst.append(val)
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
    def getrawreturnvaluedict(self, localunprocessedcsvpathname = ''):
            print 'staring getrawreturnvaluedict'
            import os, time
            import datetime
            import csv
            import re
            import mytools
            import config
            otools = mytools.general()
            localprocessedfolder = config.localunprocessedfolder + '\\barclays\\Ready for daily processing'
            mybasedate8 = os.path.basename(localunprocessedcsvpathname).split('.')[0]
            print 'mybasedate8', mybasedate8
            mybasedate = datetime.datetime.strptime(mybasedate8, "%Y%m%d")
            print 'mybasedatedays', int(mybasedate.strftime("%d"))
            dayofmonth = int(mybasedate.strftime("%d"))
            mydict = {}
        #try:
            checkingon = 0
            mycolumn = -1
            #print 'checking:',localunprocessedcsvpathname
            if os.path.isfile(localunprocessedcsvpathname) == True:
                #print 'exists: ', localunprocessedcsvpathname

                
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(localunprocessedcsvpathname)
                #print "last modified: %s" % time.ctime(mtime)
                #datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
                                                                            #Thu Mar 16 05:16:24 2017
                filedatetime_date = datetime.datetime.strptime(time.ctime(mtime), '%a %b %d %H:%M:%S %Y')
                filedatetime = filedatetime_date.strftime('%Y-%m-%d %H.%M.%S')
                #print filedatetime
                
                with open(localunprocessedcsvpathname, 'r') as f:
                    
                    reader = csv.reader(f, dialect='excel', delimiter='\t')
                    filename = f.name
                    #print 'got here 1', filename
                    for row in reader:
                        #print len(row),row, 'xxxxxxxx'
                        if 'MTD Total' in str(row):
                            #print 'found MTD Total *******************'
                            #print str(row)
                            #print 'found Value *******************'
                            
                            mycharindex =  [ (i.start(), i.end()) for i in re.finditer('MTD Total', str(row))]
                            #print mycharindex
                            mycharindex_string = str(mycharindex[0])
                            mycharindex_string = mycharindex_string.replace('(','')
                            mycharindex_string = mycharindex_string.replace(')','')
                            mycharindex_string = mycharindex_string.replace(' ','')
                            
                            mycharindex_start = int(mycharindex_string.split(',')[0])
                            
                            mycharindex_end = int(mycharindex_string.split(',')[1])
                            #print mycharindex_start,mycharindex_end,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'
                            checkingon = 1
                            
                        elif checkingon == 1:
                            #skip
                            print 'got here 2'
                            checkingon = 2
           
                        elif checkingon == 2:
                            mymarketvalue = str(row)[mycharindex_start:mycharindex_end]
                            onlydigits = mymarketvalue.replace(' ','').replace('.','').replace('-','')
                            #print 'got here 3'
                            if checkingon == 2:
                                #print str(row)
                                testsection1 = str(row)[2:len('  Financial Institutio')][:2]
                                #print 'testsection1',testsection1,'11111111111111111111111111111111111111111111111'
                                if testsection1.strip() != '':
                                    mysection1 = str(row)[2:len('  Financial Institutio')].strip()
                                    mysection1 = mysection1.replace('[','')
                                    mysection1 = mysection1.replace(']','')
                                    mysection1 = mysection1.replace('\'','')
                                    #print mysection1, '@@@@@@@@@@@@@@ Section 1 @@@@@@@@@@@@@@@@'
            
##                                testsection2 = str(row)[2:len('  Financial Institutio')][:4]
##                                #print 'testsection2',testsection2,'222222222222222222222222222222222222222222222222'
##                                if testsection2.strip() != '':
##                                    mysection2 = str(row)[2:len('  Financial Institutio')].strip()
##                                    mysection2 = mysection2.replace('[','')
##                                    mysection2 = mysection2.replace(']','')
##                                    mysection2 = mysection2.replace('\'','')
##                                    #print mysection2, '@@@@@@@@@@@@@@ Section 2 @@@@@@@@@@@@@@@@'                  
                              
                          
                          
                            if 'INDEX RESULTS' in str(row):
                                print 'break happened'
                                break
                            if len(str(row)) > mycharindex_end:
                                
                                #print str(row)[2:21],str(row)[22:31],str(row)[32:38],mymarketvalue,filename,'|||||',row[0], 'xxxxxxxx', str(row)[32:39]
                                issuename = str(row)[2:len('  Financial Institutio')]
                                issuename = issuename.replace('[','')
                                issuename = issuename.replace(']','')
                                issuename = issuename.replace('\'','')
                                #print 'got here 4',issuename
                                #if not issuename[:2] == '  ':
                                if mymarketvalue.strip().replace('-','').replace('.','').isdigit() == True:
                                    ##if mysection1 == 'U.S. Aggregate' and mysection2 == 'U.S. Aggregate':
                                    if mysection1 == 'U.S. Aggregate' and issuename.strip()== 'U.S. Aggregate':
                                        print 'got here 5'
                                        #print mysection1,mysection2,mymarketvalue.strip(),filename
                                        mydict[len(mydict)] = {'source':'barclays','category':'agg','mysection1':mysection1,'issue':issuename.strip(),'mtdreturn':mymarketvalue.strip(),'dayofmonth':dayofmonth,'filename':filename,'filedatetime':filedatetime}

            
            
            return mydict
        
            ## #####################
            ## Moves processed files
            #import os
            #localprocessedcsvpathname = os.path.join(localprocessedfolder,filename) #'E:\Batches\development\projects\Investment Strategy\ETL\Uploads\Ready'.encode('string_escape')
            #if os.path.exists(localprocessedcsvpathname):
            #    os.remove(localprocessedcsvpathname)
            #shutil.move(localunprocessedcsvpathname, localprocessedfolder)
            ## #####################
            
            
       # except Exception as e:
       #     print '*** you better write an error log ***'
       #     print e.__doc__



if __name__ == "__main__":
    import sys
    monthlyreturn = 0.39545183
    numberofmonths = 28
    #try:
    if 1 == 1:
        import os
        o = perform()
        x = o.execute(1998)
        
