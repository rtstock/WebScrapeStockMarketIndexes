

@echo off

:: This creates the Excel file.  You will need to add the manual items as well.
::C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python2\good_populate_sylvan_readyfiles.py" %*

:: This creates the csv upload file for Sylvan.
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python2\good_populate_sylvan_uploadfiles_fromexcel.py" %*
