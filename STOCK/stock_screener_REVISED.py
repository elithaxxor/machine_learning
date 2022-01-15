import pandas_datareader as web ## USE TO LOAD DATA FROM WEBSITE
import pandas as pd
import datetime as dt
import traceback
from yahoo_fin import stock_info as si

## Initilize Obj
stock_range = si.tickers_sp500()
start = dt.datetime.now()-dt.timedelta(days=365)
end = dt.datetime.now()


'''             S&P Return 
    *  Use web.DataReader to access yahoo_fin
    *  Calc Percent Change
    *  Get pct_change + 1 (1.x) and find cumaltive product by using last element of array 
'''

sp500_df = web.DataReader('^GSPC', 'yahoo', start, end)
sp500_df['Pct Change'] = sp500_df['Adj Close'].pct_change()
sp500_return = (sp500_df['Pct Change'] + 1).cumprod()[-1]
print(sp500_df.head())
print(sp500_return)
## CLOSING VALUE CHANGE DAY-DAY


'''final dataframe is used for future stock buying'''
''' Stock_Returns 
    *  Use web.DataReader to access yahoo_fin / write obj to .csv 
    *  Calc Percent Change
    *  Get pct_change + 1 (1.x) and find cumaltive product by using last element of array 
'''

return_list = []
final_df = pd.DataFrame(columns=['Ticker', 'Latest_Price', 'Score', 'PE_Ratio', 'PEG_Ratio', 'SMA_150', 'SMA_200', '52_Week_Low', '52_Week_High'])
print(final_df.head())

try:
    count = 0
    for ticker in stock_range:
        df = web.DataReader(ticker, 'yahoo', start, end)
        print(f'[STOCK RANGE DF]\n{df.head()}')
        df.to_csv(f"{ticker}.csv") # Write df Object to .CSV
        df['Pct Change'] = df['Adj Close'].pct_change()
        stock_return = (df['Pct Change'] + 1).cumprod() ## EDITED ON JAN 15
        df['Stock Return'] = stock_return
        returns_compared = round((stock_return / sp500_return), 2)
        return_list.append(returns_compared)
        count +=1
        if count == 30: break
        #print(stock_range)
        print(return_list)

        best_performers = pd.DataFrame(list(zip(stock_range, return_list)),
                                       columns=['Ticker', 'Returns Compared'])

        best_performers['Score'] = best_performers['Returns Compared'].rank(pct=True) * 100
        best_performers = best_performers[best_performers['Score'] >= best_performers['Score'].quantile(0.7)]
        print(f' [BEST-PERFORMERS] -- {best_performers}')

        for ticker in best_performers['Ticker']:
            try:
                df = pd.read_csv(f"{ticker}.csv", index_col=0)  ## load df from CSV.
                moving_averages = [150, 200]
                for ma in moving_averages:
                    df['SMA_' + str(ma)] = round(df['Adj Close'].rolling(window=ma).mean())
                    latest_price = df['Adj Close'][-1]
                    pe_ratio = float(si.get_quote_table(ticker)['PE Ratio (TTM)'])
                    print('pe_ratio', pe_ratio)
                    peg_ratio = float(si.get_stats_valuation(ticker)[1][4])
                    moving_average_200 = df['SMA_200'][-1]
                    moving_average_150 = df['SMA_150'][-1]
                    low_52week = round(min(df['Low'][-(52 * 5):]), 2)
                    score = round(best_perfomers[best_performers['Ticker'] == ticker]['Score'].tolist()[0])
                    ## conditions to accept stock we are interested in
                    condition_1 = latest_price > moving_average_150 > moving_average_200
                    condition_2 = latest_price >= (1.3 * low_52week)
                    condition_3 = latest_price >= (.75 * high_52week)
                    condition_4 = pe_ratio < 40
                    condition_5 = peg_ratio < 2

                    ## final dataframe after conditons are met.
                    if (condition_1 and condition_2 and condition_3 and condition_4 and condition_5):
                        final_df = final_df.append({'Ticker': ticker,
                                                    'Latest_Price': latest_price,
                                                    'Score': score,
                                                    'PE_Ratio': pe_ratio,
                                                    'PEG_Ratio': peg_ratio,
                                                    'SMA_150': moving_average_150,
                                                    'SMA_200': moving_average_200,
                                                    '52_Week_Low': high_52week}, ignore_index=True)
            except Exception as e:
                print(f'[{ticker}] \n, {str(e)}  \n {traceback.format_exc()}')
                pass

        final_df.sort_values(by='Score', ascending=False)
        pd.set_option('display.max_columns', 10)
        print(final_df.head())
        final_df.to_csv('final.csv')

except Exception as e:
    print('EXCEPTION IN STOCKRANGE ITER', str(e), traceback.format_exc())

'''   ## Calculate Performance ## 
    * BEST PERFORMANCE CREATES A RANKING SYSTEM, WHERE 'returns_compared' and 'score' is caculated by dividing stock_return / sp500 ^^  
    * Use .rank to compare  returns 
    * choose best_performer, in this case the top 20% earners. 
'''



'''
    * Create loop to iterate best_performer stock from above 
    * set moving_average time-frame, and create loop thorugh 
    * moving_average to calcualte  the average change in a data series over time [150, 200]
'''


## load data from csv rather than yahoo api


