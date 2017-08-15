:::::::
:: Pull

@echo off
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_download_barclays_lastfivedays.py" %*
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_download_msci.py" %*
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_download_nareit.py" %*
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_download_wilshire.py" %*
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_downloadandread_hfrx.py" %*


:::::::
:: Read


::::::::::::
::Barclays::
::::::::::::

::agg
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_agg_returnsmonthly.py" %*
:::::::  C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_agg_priceandmarketvalue.py" %*

::aggr
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_aggr_returnsmonthlypriceandmarketvalue.py" %*

::gcs
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_gcs_returnsmonthly.py" %*
:::::::  C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_gcs_priceandmarketvalue.py" %*

::hyd
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_hyd_returnsmonthly.py" %*
:::::::  C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_hyd_priceandmarketvalue.py" %*

::muni
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_muni_returnsmonthlypriceandmarketvalue.py" %*

::belw
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_barclays_belw_returnsmonthlypriceandmarketvalue.py" %*


::msci,nareit,wilshire
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_msci.py" %*
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_nareit.py" %*
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_wilshire.py" %*

::hfrs already read

:: msci daily
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_download_msci_dailyreturnsmtd.py" %*
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\Investment Strategy\Code\Python\good_readfile_msci_daily.py" %*
