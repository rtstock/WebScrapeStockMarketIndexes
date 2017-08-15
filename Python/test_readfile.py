# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 09:42:42 2015

@author: justin.malinchak
"""
filepathname = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\\Downloads\\Unprocessed\\barclays\\20150602.muni'
crs = open(filepathname, "r")
f = open(filepathname, 'r')
all_words = map(lambda l: l.split('\t'), f.readlines())
for row in all_words:
    print row

dictMTDTot = {}

import csv
mycolumn = -1
with open(filepathname, 'r') as f:
    reader = csv.reader(f, dialect='excel', delimiter='\t')
    for row in reader:
        for colid in range(len(row)):
            if row[colid] == 'MTDTot':
                mycolumn = colid
            if mycolumn > 0 and colid == mycolumn:
                #print row[1],row[mycolumn]
                dictMTDTot[len(dictMTDTot)] = 'muni',row[1],row[2],'MTDTot',row[mycolumn]
print 'mycolumn=',mycolumn
for k,v in dictMTDTot.items():
    print k,v
