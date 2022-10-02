#################################################
########## Stock prices data crawler ############
#################################################
########## Written by Renaud Axel Eba ###########
##########       2022/05/10           ###########
#################################################


import datetime           
import time                
import pandas as pd       

class CrawlStockPrices(object):
    def __init__(self):###Constructor of CrawlStockPrices class
        self.base_url = "https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={start_time}&period2={end_time}&interval={interval}&events=history&includeAdjustedClose=true"
        self.interval = "1d"

    def __build_url(self, ticker, period_start, period_end):###building the url request with the good parameters passed on
        return self.base_url.format(ticker=ticker, start_time=period_start, end_time=period_end, interval=self.interval)

    def get_ticker_data(self, ticker, period_start, period_end):
        ###In this function, i am passing the ticker value, the start and end time periods of our dataset
        epoch_start = int(time.mktime(period_start.timetuple()))###Converts the date type into integer type as expected by Yahoo Finance
        epoch_end = int(time.mktime(period_end.timetuple()))

        return pd.read_csv(self.__build_url(ticker, epoch_start, epoch_end))

if __name__ == '__main__':###Main program to be executed
    dh = CrawlStockPrices()
    ### AAPL --> Apple Inc. (IT sector)
    ### SMSN.IL --> Samsung Electronics Limited (IT sector)
    ### TSLA --> Tesla Inc.
    ### BAC --> Bank Of America Corporation (Financial sector)
    ### JPM --> JPMorgan Chase & Co
    ### BCS --> Barclays PLC
    
    tickers_list=['TSLA','AAPL','SMSN.IL','BAC','JPM','BCS']
### Taking the training dataset
    for i in range (len(tickers_list)):
        df = dh.get_ticker_data(tickers_list[i], datetime.datetime(2015, 1, 1), datetime.datetime(2022, 6, 25))
        df.head()
        df=pd.DataFrame(df)
        df.to_csv(r'C:\Users\HP\Documents\Courses\Handong God University\Master Thesis materials\ML previous works\\'+tickers_list[i]+'_TrainingDataset.csv',index=False)
### Taking the test dataset
     #for i in range (len(tickers_list)):
      #  df = dh.get_ticker_data(tickers_list[i], datetime.datetime(2021, 1, 1), datetime.datetime(2022, 5, 1))
       # df.head()
        #df=pd.DataFrame(df)
        #df.to_csv(r'C:\Users\HP\Documents\Courses\Handong God University\Master Thesis materials\ML previous works\\'+tickers_list[i]+'_TestDataset.csv',index=False)
        
