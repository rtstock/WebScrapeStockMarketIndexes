

@echo off
:: SUSPENDED: good_populate_sylvan_readyfiles.py ON 3/3/2016
::    Reason: the server ipc-vapp01 needs installation of MS Excel application and the primary interop assembly (PIA) to run.  
::		the process updates the "prep sheet" that Victor had used in the past.
::		what is actually needed is the good_populate_sylvan_uploadfiles.py.
:: C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_populate_sylvan_readyfiles.py" %*

C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_populate_sylvan_uploadfiles.py" %*
