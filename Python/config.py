# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 09:44:24 2015

@author: justin.malinchak
"""

serverwatcherdestination = '\\\\ipc-vsql01\\data\\Batches\\prod\\WatchFolder\\incoming'
serverlistenertrigger = '\\\\ipc-vsql01\\data\\Batches\\prod\\WatchFolder\\watch-for-changes-here'

localuploadsreadyfolder =     'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\\Uploads\\Ready'
#serveruploadsreadyfolder =    'E:\\Batches\\development\\projects\\Investment Strategy\\ETL\\Uploads\\Ready'
serveruploadsreadyfolder =    '\\\\IPC-VSQL01\\DATA\\Batches\\development\\projects\\Investment Strategy\\ETL\\Uploads\\Ready'
localunprocessedfolder = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\\Downloads\\Unprocessed'
localprocessedfolder =   'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\Downloads\\processed'

# Sylvan Ready Files
sylvanready_template_inputfilename = 'C:\\Batches\\ToolsDoNotDelete\\ssc excel\\%Index returns YYYY-MM inputs.xlsx'
sylvanready_destination_path = '\\\\ipcnet\\company\\misc\\Apl\\APL Benchmarks\\Data\\YYYY\\MMM'
sylvanready_daily_path = '\\\\ipcnet\\company\\misc\\Apl\\APL Benchmarks\\Data\\$Daily\\automated'
watcheroutputpath = 'C:\\Batches\\AutomationProjects\\Watcher\\output'

# earlier used connectstring_for_dataagg = "Provider=SQLNCLI10;Server=IPC-VSQL01;Initial Catalog=DataAgg;Trusted_Connection=yes;"
connectstring_for_dataagg = "DRIVER={SQL Server};Server=IPC-VSQL01;Database=DataAgg;Trusted_Connection=yes;"
# connectstring_for_dataagg = "Server=IPC-VSQL01;Database=DataAgg;Trusted_Connection=True;"
#Server=myServerAddress;Database=myDataBase;Trusted_Connection=True;
localdatafileoutputpath = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\zDataFileOutput'
