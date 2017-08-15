'''
# Notes
    Downloads last X days of Barclays data from lehman via ftp
'''
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:43:23 2015

@author: jmalinchak
"""

class perform:
    def __init__(self,
            init_param = 2
                     ):
            self.PublicVariable = 100 * init_param

    def set_PublicVariable(self,PublicVariable):
        self._PublicVariable = PublicVariable
    def get_PublicVariable(self):
        return self._PublicVariable
    PublicVariable = property(get_PublicVariable, set_PublicVariable) 

    def execute(self, download_last_x_days = -5, specificextension = '.agg.gz'):
        #################################################################################
        #download_last_x_days = -5
        #################################################################################

        from ftplib import FTP
        import os, os.path

        #directory_where_datafiles_are_downloaded='C:\\Batches\\Temp\\barclays\\'
        #old directory_where_datafiles_are_downloaded='C:\\Batches\\AutomationProjects\\Investment Strategy\\Downloads\\barclays\\'

        import config
        directory_where_datafiles_are_downloaded = os.path.join(config.localunprocessedfolder,'barclays')

        os.chdir(directory_where_datafiles_are_downloaded)
        ftp = FTP('pcdial.lehman.com')

        print 'Logging in to pcdial.lehman.com'
        ftp.login('advest', 'fred0702')

        print 'Accessing files...'

        #filenames = ftp.nlst() # get filenames within the directory
        #print filenames

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

        for key, value in sorted(dict_of_date8s.iteritems()):
            print(key, value)


        for k,refdate8 in sorted(dict_of_date8s.iteritems()):
            print 'Getting files from ',refdate8,'...'
            name = refdate8+specificextension
            local_filename = os.path.join(directory_where_datafiles_are_downloaded, name)
            file = open(local_filename, 'wb')
            try:
                ftp.retrbinary('RETR '+ name, file.write)
                print 'retrieved',name
            except Exception as e:
                print 'no file exists',name
            file.close()
            
            '''                
            for name in ftp.nlst():
                    print name
                    getthis = 0
                    if refdate8 in name:
                        if name[-4:] == '.agg':
                            getthis = 1                        
                        #if name[-5:] == '.aggr':
                        #    getthis = 1                        
                        #if name[-5:] == '.muni':
                        #    getthis = 1 
                        #if name[-4:] == '.hyd':
                        #    getthis = 1
                        #if name[-4:] == '.gcs':
                        #    getthis = 1
                        #if name[-5:] == '.belw':
                        #    getthis = 1

                        if getthis != 0:            
                            
                            local_filename = os.path.join(directory_where_datafiles_are_downloaded, name)
                            file = open(local_filename, 'wb')
                            ftp.retrbinary('RETR '+ name, file.write)
                            file.close()        
                            print 'retrieved',name
                    
            
            '''
            
        print 'downloading of files is done.'
        print 'you can find files here:',directory_where_datafiles_are_downloaded
        return directory_where_datafiles_are_downloaded

if __name__ == "__main__":
    import sys
    try:
        import os
        o = perform()
        if len(sys.argv) > 1:
            exec_result = o.execute(sys.argv[0])
        else:
            exec_result = o.execute(-3000,'.agg.gz')
        print 'result of __main__'
        print exec_result
        
            
    except Exception as e:
        print(e)
        print 'this error occurred attempting to run good_python_class_example'

