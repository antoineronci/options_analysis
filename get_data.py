from pandas_datareader import data as pdr
import yfinance as yf
import pandas as pd
yf.pdr_override




def get_all_maturities(ticker):
    ticker = yf.Ticker(ticker)
    maturities = ticker.options
    tables = len(maturities)
    for i in range(tables):
        df = ticker.option_chain(maturities[i])
        call = df.calls[['lastTradeDate','lastPrice','bid','ask','volume','openInterest','impliedVolatility','strike']]
        put = df.puts[['lastTradeDate','strike','lastPrice','bid','ask','volume','openInterest','impliedVolatility']]
        option_chain = pd.merge(call, put, how='left', left_on='strike', right_on='strike')
        with pd.ExcelWriter('option_chain_analysis.xlsm',mode='a') as writer:
            option_chain.to_excel(writer, sheet_name=str(maturities[i]))
        print(i)

ticker = input('enter a ticker: ')
get_all_maturities(ticker)
        
        
  
        
    
    
        
