class procedure:

    def __init__(self,
           # procname = 'no_name'
           # , params = {}
                     ):
        print 'started perform.__init__'
        
    def execute(self):
        import datetime
        today_date = datetime.date.today()
        from datetime import datetime
        from dateutil.relativedelta import relativedelta
        yearago_date = today_date + relativedelta(years=-1)
        yearago_date = yearago_date + relativedelta(months=-1)
        print today_date
        print yearago_date
        import pandas_datareader.data as pdr
        result = pdr.DataReader("DGS1", "fred", yearago_date, today_date)
        return result
    
if __name__ == "__main__":
    o = procedure()
    df = o.execute()
    print df
    import datetime
    today_date = datetime.date.today()
    path_to_download_folder = "\\\\ipcnet\\company\\misc\\Apl\\APL Benchmarks\\Data\\FRED Treasury downloads\\"
    csv_filepath = path_to_download_folder +'One Year Constant Maturity (Daily) ' + str(today_date) + '.csv'
    df.to_csv(path_or_buf=csv_filepath, sep=',')
