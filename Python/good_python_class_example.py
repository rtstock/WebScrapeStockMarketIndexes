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

    def execute(self, param0 = 3, param1 = 4):

        #try:
            self.PublicVariable = (self.PublicVariable * param0) + param1
            val = self.PublicVariable  + param1
            return val
        
            ## #####################
            ## Moves processed files
            #import os
            #localprocessedcsvpathname = os.path.join(localprocessedfolder,filename) #'E:\Batches\development\projects\Investment Strategy\ETL\Uploads\Ready'.encode('string_escape')
            #if os.path.exists(localprocessedcsvpathname):
            #    os.remove(localprocessedcsvpathname)
            #shutil.move(localunprocessedcsvpathname, localprocessedfolder)
            ## #####################
            
            
       # except Exception as e:

if __name__ == "__main__":
    import sys
    try:
        import os
        o = perform()
        if len(sys.argv) > 1:
            exec_result = o.execute(sys.argv[0],sys.argv[1])
        else:
            exec_result = o.execute(7,8)
        print 'result of __main__',exec_result
        #return exec_result
            
    except Exception as e:
        print(e)
        print 'this error occurred attempting to write to changethis.txt'
