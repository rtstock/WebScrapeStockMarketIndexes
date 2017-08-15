

@echo off

::::::::::::
::Barclays::
::::::::::::

::agg
C:\Users\Justin.Malinchak\AppData\Local\Continuum\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_agg_returnsmonthly.py" %*
C:\Users\Justin.Malinchak\AppData\Local\Continuum\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_agg_priceandmarketvalue.py" %*

::aggr
C:\Users\Justin.Malinchak\AppData\Local\Continuum\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_aggr_returnsmonthlypriceandmarketvalue.py" %*

::gcs
C:\Users\Justin.Malinchak\AppData\Local\Continuum\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_gcs_returnsmonthly.py" %*
C:\Users\Justin.Malinchak\AppData\Local\Continuum\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_gcs_priceandmarketvalue.py" %*

::hyd
C:\Users\Justin.Malinchak\AppData\Local\Continuum\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_hyd_returnsmonthly.py" %*
C:\Users\Justin.Malinchak\AppData\Local\Continuum\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_hyd_priceandmarketvalue.py" %*

::muni
C:\Users\Justin.Malinchak\AppData\Local\Continuum\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_muni_returnsmonthlypriceandmarketvalue.py" %*

::msci,nareit,wilshire
C:\Users\Justin.Malinchak\AppData\Local\Continuum\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_msci.py" %*
C:\Users\Justin.Malinchak\AppData\Local\Continuum\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_nareit.py" %*
C:\Users\Justin.Malinchak\AppData\Local\Continuum\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_wilshire.py" %*

::hfrs already read