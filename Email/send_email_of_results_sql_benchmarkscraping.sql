sp_CONFIGURE 'show advanced', 1
GO
RECONFIGURE
GO
sp_CONFIGURE 'Database Mail XPs', 1
GO
RECONFIGURE
GO
USE msdb
GO

declare @date_ProductValues datetime
declare @date7_LastPeriod varchar(7)
declare @count_SourcesCompleted int

-- select MAX(Last_Update) from DataAgg..GWP_Accounts 

declare @lastfiledate_ProductValues datetime
declare @lastfiledate_ProductValues_Daily datetime
declare @lastfiledate_ProductValues_Mtd datetime

declare @result_ProductValues varchar(50)
declare @result_ProductValues_Daily varchar(50)
declare @result_ProductValues_Mtd varchar(50)

set @lastfiledate_ProductValues = (select max(SourceFileDate) from DataAgg.dbo.ProductValues)
set @lastfiledate_ProductValues_Daily = (select max(SourceFileDate) from DataAgg.dbo.ProductValues_Daily)
set @lastfiledate_ProductValues_Mtd = (select max(SourceFileDate) from DataAgg.dbo.ProductValues_Mtd)

declare @totalresult int
set @totalresult = 0
if convert(date, @lastfiledate_ProductValues) = CONVERT(date, getdate())
	begin
	set @result_ProductValues = 'ok IPC-VSQL01.DataAgg..ProductValues'
	set @totalresult = @totalresult + 1
	end
if convert(date, @lastfiledate_ProductValues_Daily) = CONVERT(date, getdate())
	begin
	set @result_ProductValues_Daily = 'ok IPC-VSQL01.DataAgg..ProductValues_Daily'
	set @totalresult = @totalresult + 1
	end
if convert(date, @lastfiledate_ProductValues_Mtd) = CONVERT(date, getdate())
	begin
	set @result_ProductValues_Mtd = 'ok IPC-VSQL01.DataAgg..ProductValues_Mtd'
	set @totalresult = @totalresult + 1
	end
	
select 
	@date_ProductValues = 
	MAX(SourceFileDate) 
from DataAgg..ProductValues 

select 
	@date7_LastPeriod = 
	MAX(Period )
from DataAgg..ProductValues 


select 
	@count_SourcesCompleted = 
	COUNT(*)
from
(
	select distinct SourceName
	from DataAgg..ProductValues 
	where Period = @date7_LastPeriod
) A
/*
	select distinct SourceName
	from DataAgg..ProductValues 
	order by SourceName
	where Period = '2015-09'
	order by SourceName

--print @date_ProductValues 
--print @date7_LastPeriod 
--print @count_SourcesCompleted 

Barclays (agg)
Barclays (aggr)
Barclays (belw)
Barclays (gcs)
Barclays (hyd)
Barclays (muni)
MSCI
NAREIT
Wilshire

select * from DataAgg..ProductValues where SourceName = 'HFRX'
select * from DataAgg..ProductValues_Mtd where SourceName = 'HFRX' order by Period Desc
select * from DataAgg..ProductValues_Daily where SourceName = 'HFRX' order by Period Desc

*/
declare @BodyText varchar(max)
set  @BodyText ='Database table automatic update notice:'
	+ CHAR(10) 
	+ CHAR(10) 
	+ '  ' + char(149) + '  ' + @@SERVERNAME + '.DataAgg..ProductValues'
	+ CHAR(10) 
	+ '  ' + char(149) + '  ' + 'Last updated on: ' + convert(varchar(23),@date_ProductValues) 
	+ CHAR(10) 
	+ '  ' + char(149) + '  ' + 'Latest period: ' + @date7_LastPeriod
	+ CHAR(10) 
	+ '  ' + char(149) + '  ' + 'Total Sources updated for latest period: ' + convert(varchar,@count_SourcesCompleted)
	+ CHAR(10) 
	+ '  ' + char(149) + '  ' + '----------------------------'
	+ CHAR(10) 
	+ '  ' + char(149) + '  ' + @result_ProductValues
	+ CHAR(10) 
	+ '  ' + char(149) + '  ' + @result_ProductValues_Daily
	+ CHAR(10) 
	+ '  ' + char(149) + '  ' + @result_ProductValues_Mtd	
	+ CHAR(10)
	+ CHAR(10)
	+'Source: E:\DATA\Batches\development\projects\Investment Strategy\ETL\code\send_email_of_results_sql.sql'

declare @SubjectString varchar(100)
set @SubjectString = 'Job: Screen Scraping ' + case when @totalresult = 3 then 'SUCCESS ' ELSE 'FAIL ' END + replace(CONVERT(varchar,@date_ProductValues,111),'/','-')
print '--------------------------'
print 'Subject: ' + @SubjectString 
print @BodyText

EXEC sp_send_dbmail @profile_name='IPC Mail Profile',
@recipients='justin.malinchak@ipcanswers.com;victor.sanders@ipcanswers.com',
@subject=@SubjectString,
@body=@BodyText

-- select convert(varchar,Getdate(),109)

-- exec sysmail_help_queue_sp @queue_type = 'Mail' ;
-- select * from sysmail_event_log
-- select * from sysmail_allitems
-- The mail could not be sent to the recipients because of the mail server failure. (Sending Mail using Account 1 (2016-03-03T11:21:24). Exception Message: Cannot send mails to mail server. (The remote certificate is invalid according to the validation procedure.). )
-- The mail could not be sent to the recipients because of the mail server failure. (Sending Mail using Account 1 (2016-02-27T08:00:37). Exception Message: Cannot send mails to mail server. (The SMTP server requires a secure connection or the client was not authenticated. The server response was: 5.7.1 Client was not authenticated). )
-- The mail could not be sent to the recipients because of the mail server failure. (Sending Mail using Account 1 (2016-02-29T19:01:53). Exception Message: Cannot send mails to mail server. (The SMTP server requires a secure connection or the client was not authenticated. The server response was: 5.7.1 Client was not authenticated). )
-- The mail could not be sent to the recipients because of the mail server failure. (Sending Mail using Account 1 (2016-03-03T11:20:24). Exception Message: Cannot send mails to mail server. (The remote certificate is invalid according to the validation procedure.). )
-- The mail could not be sent to the recipients because of the mail server failure. (Sending Mail using Account 1 (2016-03-03T11:21:24). Exception Message: Cannot send mails to mail server. (The remote certificate is invalid according to the validation procedure.). )
-- The mail could not be sent to the recipients because of the mail server failure. (Sending Mail using Account 1 (2016-03-03T13:50:49). Exception Message: Cannot send mails to mail server. (The remote certificate is invalid according to the validation procedure.). )
-- The mail could not be sent to the recipients because of the mail server failure. (Sending Mail using Account 1 (2016-03-03T14:04:35). Exception Message: Cannot send mails to mail server. (The remote certificate is invalid according to the validation procedure.). )
-- The mail could not be sent to the recipients because of the mail server failure. (Sending Mail using Account 1 (2016-03-03T14:06:01). Exception Message: Cannot send mails to mail server. (The remote certificate is invalid according to the validation procedure.). )
-- The mail could not be sent to the recipients because of the mail server failure. (Sending Mail using Account 1 (2016-03-03T14:07:30). Exception Message: Cannot send mails to mail server. (The remote certificate is invalid according to the validation procedure.). )
-- The mail could not be sent to the recipients because of the mail server failure. (Sending Mail using Account 1 (2016-03-03T14:10:39). Exception Message: Cannot send mails to mail server. (The remote certificate is invalid according to the validation procedure.). )





