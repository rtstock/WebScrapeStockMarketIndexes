echo off

::-----------------------------
:: First Set the main variables
Set AppDir=E:\DATA\Batches\development\projects\Investment Strategy\ETL\code
::Set DestDir=E:\Data\GWP_Extracts

echo AppDir set to: %AppDir%
echo DestDir set to: %DestDir%

::---------------------------------------
:: Get today's date in 8 character format
set datetoday8=%date:~10,4%%date:~4,2%%date:~7,2%

	:: ====================
	:: For testing only
	::set datetoday8=20150420
	:: ====================
echo Today in 8 characters is %datetoday8%

::-------------------------------------------
:: Executes sql file to load data to database
sqlcmd -E -S IPC-VSQL01 -i "%AppDir%\send_email_of_results_sql.sql"
goto success_exit

::--------------------
:: Exit on success
:success_exit