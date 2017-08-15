#!/usr/bin/python
import ftplib
import os
pathtofile = r"P:\\Apl\\APL Benchmarks\\Data\\$Daily\\automated"
filename = "HFRXGI-D 2017-03-22 12.22.36.csv"
workingpath = 'C:\\Batches\\AutomationProjects\\Watcher\\output'
import shutil
srcfile = os.path.join(pathtofile,filename) 
dstfile = os.path.join(workingpath,'IDX_IPC_20170322.csv')
print dstfile
shutil.copy(srcfile,dstfile)

ftp = ftplib.FTP("ftp.sscgateway.com")
ftp.login("SSC519", "G2343DRTA")
ftp.cwd("/usr/ssc519/SSIS/Index")
os.chdir(workingpath)
myfile = open(dstfile, 'r')
ftp.storlines('STOR ' + dstfile, myfile)
myfile.close()
