import yfinance as yf
import streamlit as st
import datetime as dt
import altair as alt
from datetime import datetime, timedelta
import pandas as pd
import PIL
from PIL import Image
from datetime import date

import pandas_datareader as web
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas_datareader as web ## USE TO LOAD DATA FROM WEBSITE
import pandas as pd
import numpy as np
import datetime as dt
import traceback
from yahoo_fin import stock_info as si
import io
import json




image = Image.open('wsb.png')
st.image(image, use_column_width=True)
st.write('''
    #  Why *Invest* when you could **SPECULATE**! [copyleft - all wrongs reserved] - 
    https://github.com/elithaxxor?tab=repositories
    ***  ''')

#def main():
end = dt.datetime.now() - dt.timedelta(days=365)
start = dt.datetime.now()
stock_range = si.tickers_sp500()
print(type(stock_range))
end0 = dt.timedelta(days=365)
start_date = st.date_input('Start date', start)
end_date = st.date_input('End date', end)
requested_amt = (end_date - start_date) / 5
requested_amt = abs(int(requested_amt.days))

print('User Start Date', start_date)
print('User End Date', end_date)
print('req_amt', requested_amt)

#st.sidebar.header('User Selections')
#selected_stock = st.sidebar.selectbox('Year', range(len(stock_range)))
# selected_stock01 = st.sidebar.selectbox('start date', range(start_date - end_date))
# selected_year = st.sidebar.selectbox('Year', list(reversed(range(2022 - 1990))))

def main()
try:
    sp500_df = web.DataReader('^GSPC', 'yahoo', end_date, start_date)
    sp500_df['Pct Change'] = sp500_df['Adj Close'].pct_change()
    sp500_return = (sp500_df['Pct Change'] + 1).cumprod()[-1]

    print(sp500_df.head(requested_amt))
    print(sp500_return)
    print(stock_range)

    st.subheader(f's&p 500: [{requested_amt}] values, per date-time request.')
    st.write(sp500_df.head(requested_amt))
    st.subheader(f'[S&P500]-- [{requested_amt}] -- Days] ')
    st.line_chart(sp500_df.head(requested_amt))

    st.subheader('S&P 500 Return')
    st.write(sp500_return)
    st.subheader('sp500 ')
    st.write(sp500_df)
    st.subheader('Available Equities: ')
    st.write(stock_range)

    sp500_file = f"sp500 {date.today()} + best_performance.csv"
    sp500_df.to_csv(sp500_file)  # Write df Object to .CSV
    with open(sp500_file, 'rb') as f:
        st.download_button(label='Download Stock Csv', data=f, file_name=sp500_file, on_click=True)

    final_df = pd.DataFrame(
        columns=['Ticker', 'Latest_Price', 'Score', 'PE_Ratio', 'PEG_Ratio', 'SMA_150', 'SMA_200', '52_Week_Low',
                 '52_Week_High'])
    count = 0
    counter = 0
    return_list = []
    for ticker in stock_range:
        df = web.DataReader(ticker, 'yahoo', end_date, start_date)
        try:
            st.line_chart(df.head(requested_amt))
        except:
            pass
        df['Ticker'] = ticker
        df['Pct Change'] = df['Adj Close'].pct_change()
        stock_return = (df['Pct Change'] + 1).cumprod()  ## EDITED ON JAN 15
        df['Stock Return'] = stock_return
        returns_compared = round((stock_return / sp500_return), 2)
        return_list.append(returns_compared)
        df.reset_index()
        print(f'[{ticker}]\n [{end_date}]::[{start_date}] {df.head()}')
        st.subheader(f'[{ticker}] --Stock Datas-- [{requested_amt}] -- Days] ')
        st.write(df.head(requested_amt))
        try:
            st.line_chart(df.head(requested_amt))
        except:
            pass

        df_file = f"{ticker} + {date.today()} + best_performance.csv"
        df.to_csv(df_file)  # Write df Object to .CSV

        with open(df_file, 'rb') as f:
            st.download_button(label='Download Stock Csv', data=f, file_name=df_file, key=count+1, on_click=True)

        print('processing', ticker)
        print(return_list)
        counter +=1
        if counter == 35:
            print('have reached the break')
            break
        print('have reached the break')
        print(return_list)
        try:
            best_performers = pd.DataFrame(list(zip(stock_range, return_list)),
                                           columns=['Ticker', 'Returns Compared'])
            # df.dropna(axis=0)
            # df.dropna(axis=1)
            # df.fillna(0)
            # df.reset_index(inplace=True)
            # #df.best_performers.dropna()
            # df.best_performers.dropna(axis=0)
            # df.best_performers.dropna(axis=1)
            # df.best_performers.fillna(0)
            # df.best_performers.reset_index(inplace=True)
            # best_performers['Returns Compared'] = best_performers['Returns Compared'] * 100
            best_performers['Returns Compared'] = best_performers['Returns Compared']
            best_performers['Score'] = best_performers['Returns Compared'].sort_values(ascending=True)
            st.subheader(f' Performance Calculation: {ticker}]\n [{start}]::[{end}] {date.today()}')
            st.write(best_performers.head(requested_amt))
            print(f'[{ticker}]\n [{start}]::[{end}]\n {best_performers.head()}')

            print(f' [BEST-PERFORMERS] -- {best_performers}')
            st.header(f'[Best Performer] [{start}]::[{end}] ---- {date.today()}')
            st.write(best_performers.head(requested_amt))
            performance_file = f"{ticker} + best_performance.csv"
            df.to_csv(performance_file)  # Write df Object to .CSV
            count+=1

            with open(performance_file, 'rb') as f:
                st.download_button(label='Download Stock Csv', data=f, key=count+2, file_name=performance_file, on_click=True)

            for ticker in best_performers['Ticker']:
                try:
                    df = pd.read_csv(f"{ticker}.csv", index_col=0)  ## load df from CSV.
                    print('X' * 50)
                    print(f'[{ticker}]\n [{start}]::[{end}] {df.head()}')
                    print(df.head())
                    st.subheader(f'[{ticker}]\n [{end_date}]::[{start_date}] {date.today()}')
                    st.write(df.head(requested_amt))
                    st.subheader(f'[{ticker}] --Best Performers-- [{requested_amt}] -- Days] ')
                    st.line_chart(df.head(requested_amt))

                    moving_averages = [150, 200]
                    for ma in moving_averages:
                        print('[Moving-Average]', ma)
                        print(type(ma))
                        df['SMA_' + str(ma)] = round(df['Adj Close'].rolling(window=ma).mean())
                        latest_price = df['Adj Close'][-1]
                        pe_ratio = float(si.get_quote_table(ticker)['PE Ratio (TTM)'])
                        print('pe_ratio', pe_ratio)
                        peg_ratio = float(si.get_stats_valuation(ticker)[1][4])
                        moving_average_200 = df['SMA_200'][-1]
                        moving_average_150 = df['SMA_150'][-1]
                        low_52week = round(min(df['Low'][-(52 * 5):]), 2)
                        high_52week = round(min(df['High'][-(52 * 5):]), 2)
                        score = round(best_performers[best_performers['Ticker'] == ticker]['Score'].tolist()[0])
                        ## conditions to accept stock we are interested in
                        condition_1 = latest_price > moving_average_150 > moving_average_200
                        condition_2 = latest_price >= (1.3 * low_52week)
                        condition_3 = latest_price >= (.75 * high_52week)
                        condition_4 = pe_ratio < 40
                        condition_5 = peg_ratio < 2

                        st.subheader(f'Moving Averages Calculation \n, [{ticker}]\n [{end_date}]::[{start_date}] {date.today()}')
                        st.write(df.head(requested_amt))
                        st.subheader(f'[{ticker}]-- [{requested_amt}] -- Days] ')
                        st.line_chart(df.head(requested_amt))

                        ma_file = f"{ticker} + {date.today()} +moving_avg.csv"
                        df.to_csv(ma_file)  # Write df Object to .CSV
                        count+=1
                        with open(ma_file, 'rb') as f:
                            st.download_button(label='Download Stock Csv', data=f, key=count+3, file_name=ma_file, on_click=True)

                        print('X' * 50)
                        print(f'[{ticker}]\n [{start}]::[{end}] {df.head()}')
                        print(df.head())
                        print()
                        st.write(df.head(requested_amt))
                        st.subheader(f'[{ticker}]-- [{requested_amt}] -- Days] ')
                        st.line_chart(df.head(requested_amt))

                        ## final dataframe after conditons are met.
                        if (condition_1 and condition_2 and condition_3 and condition_4 and condition_5):
                            final_df = final_df.append({'Ticker': ticker,
                                                        'Latest_Price': latest_price,
                                                        'Score': score,
                                                        'PE_Ratio': pe_ratio,
                                                        'PEG_Ratio': peg_ratio,
                                                        'SMA_150': moving_average_150,
                                                        'SMA_200': moving_average_200,
                                                        '52_Week_Low': low_52week,
                                                        '52_Week_High': high_52week}, ignore_index=True)
                            try:
                                final_df.sort_values(by='Score', ascending=False)
                                pd.set_option('display.max_columns', 10)
                                print(final_df.head())

                                final_file = f'{date.today()} +final.csv'
                                final_df.to_csv(final_file)
                                st.subheader(f'Final Df \n,[{ticker}]\n --[FINAL DF W/ CALCULATIONS]-- [{end_date}]::[{start_date}] {date.today()}')
                                st.write(final_df.head(requested_amt))
                                st.subheader(f'[{ticker}]--[FINAL DF W/ CALCULATIONS]-- [{requested_amt}] -- Days] ')
                                st.line_chart(final_df.head(requested_amt))

                                with open(final_file, 'rb') as f:
                                    st.download_button(label='Download Stock Csv', data=f, file_name=final_file,
                                                       key=count + 4, on_click=True)

                            except Exception as e:
                                print('EXCEPTION IN STOCKRANGE ITER', str(e), traceback.format_exc())
                                pass
                except Exception as e:
                    print(f'[{ticker}] \n, {str(e)}  \n {traceback.format_exc()}')
                    pass
        except Exception as e:
            print(f'[{ticker}] \n, {str(e)}  \n {traceback.format_exc()}')
            pass

except Exception as e:
    print(f' [Main Loop Broken] \n, {str(e)}  \n {traceback.format_exc()}')
    pass


#main()


## more info (quote table)


#tickerSymbol = 'googl'
# financials = si.get_financials(tickerSymbol)
# financials_df = pd.DataFrame(financials)
# print(financials_df.head())
# print(type(financials_df))


# quote_table = f'{si.get_quote_table(tickerSymbol)}'
# res = json.loads(si.get_quote_table(tickerSymbol))
# print(res)


#

# quote_table = io.StringIO(quote_table)
# df = pd.read_csv(quote_table, sep=":")
# print(df.head())
# print(quote_table)
# print(type(quote_table))
#
# quote_df = pd.DataFrame(data=quote_table)
# print(quote_df.head())
#

#
# stock_range = si.tickers_sp500()
# start = dt.datetime.now()-dt.timedelta(days=365)
# end = dt.datetime.now()
#
#
# '''             S&P Return
#     *  Use web.DataReader to access yahoo_fin
#     *  Calc Percent Change
#     *  Get pct_change + 1 (1.x) and find cumaltive product by using last element of array
# '''
#
# sp500_df = web.DataReader('^GSPC', 'yahoo', start, end)
# sp500_df['Pct Change'] = sp500_df['Adj Close'].pct_change()
# sp500_return = (sp500_df['Pct Change'] + 1).cumprod()[-1]
# print(sp500_df.head())
# print(sp500_return)
#
#
# ticker = 'aapl'
# df = web.DataReader(ticker, 'yahoo', start, end)
# moving_averages = [150, 200]
# for ma in moving_averages:
#     df['SMA_' + str(ma)] = round(df['Adj Close'].rolling(window=ma).mean())
#     latest_price = df['Adj Close'][-1]
#     pe_ratio = float(si.get_quote_table(ticker)['PE Ratio (TTM)'])
#     print('pe_ratio', pe_ratio)

