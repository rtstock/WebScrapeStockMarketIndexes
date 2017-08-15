

@echo off
python C:\Batches\MyPython\DataAgg\execute_barclays_downloadfiles.py %*
python C:\Batches\MyPython\DataAgg\execute_barclays_readfiles.py %*
python C:\Batches\MyPython\DataAgg\execute_msci_etl.py %*
python C:\Batches\MyPython\DataAgg\execute_nareit_etl.py %*
python C:\Batches\MyPython\DataAgg\execute_wilshire_etl.py %*
python C:\Batches\MyPython\DataAgg\execute_hfrx_etl.py %*
