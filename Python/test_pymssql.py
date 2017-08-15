# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:38:23 2015

@author: Justin.Malinchak
"""

import adodbapi
conn = adodbapi.connect("Provider=SQLNCLI10;Server=IPC-VSQL01;Initial Catalog=DataAgg;Trusted_Connection=yes;")
#conn = adodbapi.connect(r'Server=ipc-vsql01;Database=DataAgg;Trusted_Connection=True;')
#conn.adoConn.CursorLocation = adodbapi.adUseServer
curs = conn.cursor()
query = "Select * from ProductValues_Mtd;"
curs.execute(query)
results = curs.fetchall()
for r in results:
    print r
conn.close
#import pymssql
#c = pymssql.connect(host = r'ipc-vsql01\dataagg',
#                    user = 'justin.malinchak',
#                    password = 'zg14Bn*1082')