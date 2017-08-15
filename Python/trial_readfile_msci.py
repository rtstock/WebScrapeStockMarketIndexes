# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 12:37:02 2015

@author: justin.malinchak
"""

outputfile = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\Uploads\\Files Ready For Upload\\test6.csv'

from xlrd import open_workbook
import os    
dirtocheck = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\Downloads\\msci\\'

files = os.listdir(dirtocheck)
mydict = {}
smalldict = {}
for filename in files:
    fullpath = os.path.join(dirtocheck, filename)
    lsfilename = filename.split(' ')
    nameofdata = lsfilename[0]
    dateofdata = lsfilename[1]
    categoryofdata = lsfilename[2].replace('.xls','')
    print fullpath
    wb = open_workbook(fullpath)
    values = []
    for s in wb.sheets():
        #print 'Sheet:',s.name
        headerrow = -1
        headercol = -1
        for row in range(1, s.nrows):        
            col_names = s.row(row)
            col_value = []
            for name, col in zip(col_names, range(s.ncols)):
                value  = (s.cell(row,col).value)
                if value == 'MSCI Index':
                    headerrow = row
                    headercol = col
                if headerrow > 0:
                    rowheadertext = (s.cell(row,headercol).value)
                    colheadertext = (s.cell(headerrow,col).value)
                    if len(rowheadertext) == 0:
                        headerrow = -1
                
                    if headerrow > 0 and row > headerrow and col > headercol and len(colheadertext) > 0:
                        productname = rowheadertext
                        periodtext = colheadertext
                        datavalue = s.cell(row,col).value
                        #print nameofdata,dateofdata,categoryofdata,productname,periodtext,datavalue 
                        smalldict = {'a_nameofdata':nameofdata,'b_dateofdata':dateofdata,'c_categoryofdata':categoryofdata,'d_productname':productname,'e_periodtext':periodtext,'f_datavalue':datavalue,'g_filename':filename}
                        mydict[len(mydict)] = smalldict
#            value  = (s.cell(row,col).value)
#            if headerrow == 0 :
#                if 'MSCI Index' in str(value):
#                    headerrow = row
#                    print headerrow
#            if headerrow != 0:
#                print range(row, col)
#                try : value = str(value)
#                except : pass
#                col_value.append((name.value, value))
#        values.append(col_value)
#print values
          

#import csv
#listWriter = csv.DictWriter(
#   open('C:\\Batches\\AutomationProjects\\Investment Strategy\\Uploads\\Files Ready For Upload\\test2.csv', 'wb'),
#   #fieldnames=mydict[0].keys(),
#   fieldnames=mydict[0].keys(),
#
#   delimiter=',',
#   quotechar='|',
#   quoting=csv.QUOTE_MINIMAL
#)
#
#for k,v in mydict.items():
#    print v
#    listWriter.writerow(v)
#    
#listWriter.close()

import csv

#my_dict = {"test": 1, "testing": 2}

with open(outputfile, 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, mydict[0].keys())
    w.writeheader()
    for k,v in mydict.items():
        w.writerow(v)
#
#import csv
#keys = mydict[0].keys()
#print keys
#with open('C:\\Batches\\AutomationProjects\\Investment Strategy\\Uploads\\Files Ready For Upload\\test.csv', 'wb') as output_file:
#    dict_writer = csv.DictWriter(output_file, keys)
#    dict_writer.writeheader()
#    dict_writer.writerows(mydict)