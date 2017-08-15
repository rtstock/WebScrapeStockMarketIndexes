# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:38:23 2015

@author: Justin.Malinchak
"""
import shutil
import datetime
import ntpath  
import os

class perform:
         
    def copyFile(src, dest):
        try:
            shutil.copy(src, dest)
        # eg. src and dest are the same file
        except shutil.Error as e:
            print('Error: %s' % e)
        # eg. source or destination doesn't exist
        except IOError as e:
            print('Error: %s' % e.strerror)
    
    def get_sheet_by_name(book, name):
        """Get a sheet by name from xlwt.Workbook, a strangely missing method.
        Returns None if no sheet with the given name is present.
        """
        # Note, we have to use exceptions for flow control because the
        # xlwt API is broken and gives us no other choice.
        import itertools
        try:
            for idx in itertools.count():
                sheet = book.get_sheet(idx)
                if sheet.name == name:
                    return sheet
        except IndexError:
            return None
            
    
    def last_day_of_month(date):
        if date.month == 12:
            return date.replace(day=31)
        return date.replace(month=date.month+1, day=1) - datetime.timedelta(days=1)

    def path_leaf(path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)
    
    def assure_path_exists(path):
            dir = os.path.dirname(path)
            if not os.path.exists(dir):
                    os.makedirs(dir)
    
    
    def __init__(self,
                     custommonthdate7 
                     ):
                         
        self._setup(
                     custommonthdate7
                     )

    def _setup(self
            ,  custommonthdate7                     
                     ):   
        print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        print 'start'
        # =============
        # My Parameters
        template_inputfilename = 'C:\\Batches\\Temp\\ssc excel\\%Index returns YYYY-MM inputs.xlsx'
        destination_path = 'P:\Apl\APL Benchmarks\Data\YYYY\MMM'
        # =============
        print template_inputfilename
        
        
        listsp = [
            ('Barclays (muni)','Barclays (muni) Municipal Bond: 1 Year (1-2) (USDU)','LBM01')
            ,('Barclays (muni)','Barclays (muni) Municipal Bond (USDU)','LBMUNI')
            ,('Barclays (muni)','Barclays (muni) Municipal Bond: 3 Year (2-4) (USDU)','LBM03')
            ,('Barclays (muni)','Barclays (muni) Municipal Bond: 5 Year (4-6) (USDU)','LBM05B')
            ,('Barclays (muni)','Barclays (muni) Municipal Bond: 10 Year (8-12) (USDU)','SLMU')
            ,('Barclays (muni)','Barclays (muni) Municipal Bond: Long Bond (22+) (USDU)','LBLONG')
            ,('Barclays (muni)','Barclays (muni) 1-10 Yr Blend (1-12) (USDU)','LBBLND')
            ,('Barclays (muni)','Barclays (muni) Municipal Bond: 7 Year (6-8) (USDU)','LBM07')
        #Municipal Bond: 7 Year (6-8) (USDU)
            ,('Barclays (agg)','Barclays (agg) U.S. Aggregate','SHLAGG')
            ,('Barclays (agg)','Barclays (agg) U.S. Aggregate Intermediate','LIAGBI')
            ,('Barclays (agg)','Barclays (agg) U.S. Gov/Credit','LEHMAN')
            ,('Barclays (agg)','Barclays (agg) U.S. Gov/Credit Intermediate','SHLGCI')
            ,('Barclays (agg)','Barclays (agg) U.S. Government 1-3 Yr','LBG13')
            ,('Barclays (agg)','Barclays (agg) U.S. Treasury','LBGTSY')
        #U.S. Government
            ,('Barclays (agg)','Barclays (agg) U.S. Government Intermediate','LBGINT')
            ,('Barclays (agg)','Barclays (agg) U.S. Treasury Intermediate','LBTII')
            ,('Barclays (agg)','Barclays (agg) U.S. Credit Intermediate','LBICB')
            ,('Barclays (agg)','Barclays (agg) U.S. Agency','LBUSAB')
        
            ,('Barclays (aggr)','Barclays (aggr) U.S. Treasury: U.S. TIPS (USDU)','LBTIPS')
            ,('Barclays (gcs)','Barclays (gcs) Treasury Trsy 1-3 Year','LGT1-3')
            ,('Barclays (gcs)','Barclays (gcs) Treasury Treasury Bills','LTBILL')
            ,('Barclays (hyd)','Barclays (hyd) U.S. Corporate High Y','BCHIYD')
            ,('Barclays (hyd)','Barclays (hyd) U.S. Corporate High Y Intermediate','LBIHY')
            ,('Barclays (hyd)','Barclays (hyd) Ba','LEHHIY')
        
            ,('Barclays (belw)','Barclays (belw) U.S. Treasury Bellwethers: 2 Year (USDU)','L2YTBW')
            
            ,('MSCI','MSCI DM Gross WORLD','MSCIWD')
            ,('MSCI','MSCI DM Gross WORLD ex USA','MSCIXU')
            ,('MSCI','MSCI AC Gross ACWI','MSCIAC')
            ,('MSCI','MSCI AC Gross ACWI ex USA','MSCIAW')
            ,('MSCI','MSCI EM Gross EM (EMERGING MARKETS)','MSCIEM')
            ,('MSCI','MSCI CM Gross GOLDEN DRAGON','MSCIGD')
            ,('MSCI','MSCI DM Net EAFE','EAFENT')
            ,('MSCI','MSCI DM Net WORLD','MSCIWN')
            ,('MSCI','MSCI DM Net WORLD ex USA','MSCIXN')
            ,('MSCI','MSCI AC Net ACWI','MSCIAN')
            ,('MSCI','MSCI AC Net ACWI ex USA','MSCIAX')
            ,('MSCI','MSCI DM Gross Value EAFE Value','EAFEV')
            ,('MSCI','MSCI DM Net Value EAFE Value','EAFEVN')
            ,('NAREIT','NAREIT Equity REITs','NAREIT')
            ,('Wilshire','Wilshire REIT','WIREIT')
            ,('HFRX','HFRX Global Hedge Fund Index','HFRXGH')
            ,('HFRX','HFRX Equity Hedge Index','HFRXGI')
        
        ]
        
        #MSCI AC Gross ACWI ex USA
        
        
        
        import adodbapi
        import pandas.io.sql as psql
        
        conn = adodbapi.connect("Provider=SQLNCLI10;Server=IPC-VSQL01;Initial Catalog=DataAgg;Trusted_Connection=yes;")
        
        # ------------------------------------
        # Get the max period from the database
        import os.path
        maxperiod = ''
        query = "Select Max(Period) MaxPeriod from ProductValues where Period = '"+custommonthdate7+"';"
        
        df = psql.read_sql(query, conn)
        firstcell = df.iloc[0,0]
        print 'first cell is',df.iloc[0,0]
        if firstcell == None:
            print 'no data for month ' + custommonthdate7
        else:
            maxperiod = df.iloc[0]['MaxPeriod']
            FoundYear = int(maxperiod[:4])
            FoundMonth= int(maxperiod[-2:])
            lastdayofmaxperiod = self.last_day_of_month(datetime.date(FoundYear, FoundMonth, 1))
            lastdayofmaxperiod_formatted = lastdayofmaxperiod.strftime('%m/%d/%Y')
            print 'lastdayofmaxperiod_formatted',lastdayofmaxperiod_formatted
            year_asstring = lastdayofmaxperiod.strftime('%Y')
            shortmonthname = lastdayofmaxperiod.strftime("%B") # 'dec'
            resolved_destination_path = destination_path.replace('YYYY',year_asstring).replace('MMM',shortmonthname)
            print 'resolved_destination_path',resolved_destination_path
            
        # ---------------------
        # Get the return values
        dict_returns = {}
        if len(maxperiod) > 0:
            for item in listsp:
                query = "Select top 1 * from ProductValues where Measure = 'Returns Monthly' and SourceName = '"+item[0]+"' and ProductName = '"+item[1]+"' and Period = '"+maxperiod+"';"
                print query
                df = psql.read_sql(query, conn)
                #print df
                if len(df.index) > 0:
                    thenumber = df.iloc[0]['DataValue']
                    print item[0], '------',item[2],'------',item[1],'=',thenumber
                    dict_returns[item[2]] = thenumber
        
        
        # --------------------
        # Close the connection
        conn.close
        
        # ------------------------------------------------
        # Create the Excel file from template if necessary
        if len(maxperiod) > 0:
            print 'maxperiod:',maxperiod
            
            inputfilename = template_inputfilename.replace('YYYY-MM',maxperiod).replace('%','')
            
            month_asminimalcharacters = str(int(lastdayofmaxperiod.strftime("%m")))
            year_as2character = (lastdayofmaxperiod.strftime("%Y"))[-2:]
            resolved_destination_pathfile = resolved_destination_path + '\\' + self.path_leaf(template_inputfilename).replace('YYYY-MM',month_asminimalcharacters+'-'+year_as2character).replace('%','').replace('inputs','inputs (automated)')
        
            
            if not os.path.isfile(inputfilename):
                print 'file',inputfilename, 'does not exist'
                self.copyFile(template_inputfilename,inputfilename)
                if not os.path.isfile(inputfilename):
                    print 'tried to copy',template_inputfilename,'to make the file, but process failed.'
                else:
                    print 'ok ok, your file now exists.'
                    
            # ---------------------------------------
            # Now open the excel file and populate it
                
            # ------------------------------------------------------------------------------------
            # Couldn't find much from pandas on how to do it, you may want to look into this later 
            #    import pandas as pd
            #    xl = pd.ExcelFile(inputfilename)
            #    
            #    for sn in xl.sheet_names:
            #        print sn
            #        print sn.cells(1,18)
            #    xl.close        
                    
            # -----------------------
            # This seems to work fine
            if os.path.isfile(inputfilename):
                # ------------------------------------
                # Get the data into a dictionary first
                dict_ref = {}
                from xlrd import open_workbook
                book = open_workbook(inputfilename,on_demand=True)        
        
                sheet = book.sheet_by_name('bench')
                        
                for k,v in dict_returns.items():
                    # Attempt to find a matching row (search the first column for 'john')
                    rowIndex = -1
                    for cell in sheet.col(1): # 
                        rowIndex = rowIndex + 1
                        if k == cell.value:
                            print 'found it:',k,v,sheet.cell(rowIndex,3).value,rowIndex+1
                            dict_ref[k] = [rowIndex+1,v]
        
                # --------------------------------
                # Then populate the worksheet here
                from win32com.client import Dispatch
                xlApp = Dispatch("Excel.Application")
                xlApp.Visible = 1
                xlApp.Workbooks.Open(inputfilename)
                
                for k,v in dict_ref.items():
                    print k,v
                    xlApp.ActiveWorkbook.ActiveSheet.Cells(v[0],4).Value = v[1]
                    xlApp.ActiveWorkbook.ActiveSheet.cells(v[0],3).Value = lastdayofmaxperiod_formatted
                xlApp.ActiveWorkbook.Close(SaveChanges=1) # see note 1
                xlApp.Quit()
                xlApp.Visible = 0 # see note 2
                del xlApp
                
                self.assure_path_exists(resolved_destination_pathfile)
                self.copyFile(inputfilename,resolved_destination_pathfile)
                print 'You can find your final file here:',resolved_destination_pathfile
        ## =====================================
        #print 'my test here'
        #print '----------'
        #query = "Select * from ProductValues where SourceName = 'MSCI' and ProductName like '%USA%' and Period = '2015-05';"
        #df = psql.read_sql(query, conn)
        #print df
        ## =====================================


if __name__=='__main__':
    o = perform('2015-08') 
