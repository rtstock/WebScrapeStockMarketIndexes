class perform:
    
    def __init__(self,
           # procname = 'xdeletethis_sylvan'
           # , params = {}
                     ):
        #print 'started good_readvalue_marketvalue_barclays_aggregate.py'
            a = 100
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
        for ret in list_of_returns:
            lst.append(1.0+ret)
            z = z*(1.0+(ret/100.0))
            #print 'z',z, len(list_of_returns)
        val = (z-1.0) * 100.0
        return val
        
        #print lst
        #from scipy import stats as scistats
        #return 1.0 - scistats.gmean(lst)
    def execute(self, localunprocessedcsvpathname = ''):

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
                                        mydict[len(mydict)] = {'source':'barclays','category':'agg','mysection1':mysection1,'issue':issuename.strip(),'mtdreturn':mymarketvalue.strip(),'filename':filename,'filedatetime':filedatetime}

            
            
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
        filename = os.path.join('C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\\Downloads\\Unprocessed\\barclays\\Ready for daily processing\\','20170314.agg')
        mydict = o.execute(filename)
        for k,v in mydict.items():
            print k,v
        dailyreturnlist = o.calcdaily(monthlyreturn,numberofmonths)
        
        print dailyreturnlist
        checkendingvalue = o.calcgeomean(dailyreturnlist)
        print 'starting monthlyreturn',monthlyreturn
        print 'should be the same as monthly return',checkendingvalue
        if round(monthlyreturn,4) == round(checkendingvalue,4):
            print 'success!'
    #except Exception as e:
    #    print(e)
    #    print 'this error occurred attempting to write to changethis.txt'
