import yfinance as yf
import streamlit as st
import datetime as dt
import altair as alt
from datetime import datetime, timedelta
import pandas as pd
import PIL
from PIL import Image
import pandas_datareader as web
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


image = Image.open('wsb.png')
st.image(image, use_column_width=True)
st.write('''
    # Simple webapp to display *opening* and **closing** of stock prices.
    ***  ''')

## preprocessing
# print(tickerDf.columns)
# tickerDf = tickerDf[['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']]
# print(tickerDf.index)
# tickerDf.dropna(how='all')
# tickerDf['Date'] = tickerDf.index[0]
# tickerDf = tickerDf[['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']]
# tickerDf['Date'] = tickerDf['Date'].map(mdates.date2num)
# tickerDf.reset_index(drop=True)
# # tickerDf.reset_index(inplace=False)
# b_chart = alt.Chart(tickerDf).mark_bar().encode(x=tickerDf['Volume'], y=str(tickerDf['Date']))
# b_chart = b_chart.properties(width=alt.Step(80))
# st.write(b_chart)
#
#

def additional_data(tickerSymbol):
    st.subheader(' [5-DAY] Stock Information [DATA FRAME]')
    start = dt.datetime.now() - dt.timedelta(days=365)
    end = dt.datetime.now()

    df = web.DataReader(tickerSymbol, f'yahoo', start, end)
    df.to_csv(f"{tickerSymbol} + {dt.date.today()}.csv")  # Write df Object to .CSV
    df['Pct Change'] = df['Adj Close'].pct_change()
    df['Stock Return'] = (df['Pct Change'] + 1).cumprod()
    #df = df[['Open', 'High', 'Low', 'Close']]
    #df['Date'] = df['Date'].map(mdates.date2num)
    df.reset_index(inplace=True)

    st.subheader(' [5-DAY] Stock Information with PCT change and Return.')
    st.write(df.head())
    print(df.head())


    st.header(f'[{tickerSymbol}] [Pct Change] [{(df["Pct Change"].count())} Values] ') #volume
    st.line_chart(df['Pct Change'])

    st.header(f'[{tickerSymbol}] [Stock Return] [{(df["Stock Return"].count())} Values] ') #stock return (df[stock_return]) above
    st.line_chart(df['Stock Return'])
    st.header(f'[{tickerSymbol}] [ALL TOGETHER] [{(df["Volume"].count())} Values]') # all days values together.
    st.line_chart(df)



def graph_display(tickerSymbol):
    ''' Takes User Input and displays graphs, accordingly '''

    print('Processsing, ', tickerSymbol)
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

    st.subheader(f'{tickerSymbol} [Stock Information] ')
    print(tickerDf.head())
    st.write(tickerDf.head())

    ## Graphs
    st.subheader(f'{tickerSymbol} [Stock Information -- 5-Year] ')
    st.line_chart(tickerDf)
    st.subheader(f'[{tickerSymbol}] [Stock Information -- 2 -Year] ')
    st.line_chart(tickerDf.head(2))
    st.header(f'[{tickerSymbol}] [Volume] [{(tickerDf["Volume"].count())} Values]') #volume
    st.line_chart(tickerDf.Volume)
    st.header(f'[{tickerSymbol}] [Opening Prices] [{(tickerDf["Open"].count())}] Values') #open
    st.line_chart(tickerDf.Open)
    st.header(f'[{tickerSymbol}] [Closing Prices] [{(tickerDf["Close"].count())} Values ]') #close
    st.line_chart(tickerDf.Close)
    st.header(f'[{tickerSymbol}] [Daily High] [{(tickerDf["High"].count())} Values] ') #volume
    st.line_chart(tickerDf.Volume)

    additional_data(tickerSymbol) ## call function for addiotnal data



def main():
   # ticker = input('Enter The Stock Symbol, ex: GOOG: ')
    while True:
        stock_input = ">STOCK INPUT \n "
        print(stock_input)
        print(type(stock_input))
        stock = st.text_area('Text Area', stock_input, height=25)
        stock = stock.splitlines()
        stock = stock[1:]  # isolate the the 2nd line on list to retrieve user input
        stock = str(stock)
        stock = stock[1:-1]
        stock = stock[1:-1]
        st.write(''' *** ''')
        print(f'User Entered {stock} \n {type(stock)}')
        if stock != []:
            graph_display(stock)
            additional_data(stock)

main()




### scratches
# stock_input01 = ">STOCK INPUT \n "
# stock01 = st.text_area('Text Area', stock_input01, height=25)
# stock01 = stock01.splitlines()
# stock01 = stock01[1:]  # isolate the the 2nd line to retrieve user input
# st.write(''' *** ''')
#
# ## function recursion IF frontend recieves new stock symbol, reload page with new info
# if bool(stock01):
#     graph_display(tickerSymbol)
#     additional_data(tickerSymbol)
#
