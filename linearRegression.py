#regression 
import pandas as pd 
import Quandl 

df = Quandl.get('WIKI/GOOGL')

print(df.head())

dataframe= df[['Adj.Open', 'Adj.High', 'Adj.Low', 'Adj.Close', 'Adj.Volume']]

dataframe ['HL_PCT'] = (dataframe['Adj.High'] - dataframe['Adj.Close'])/ dataframe['Adj.Close'] *100.0 

dataframe ['PCT_Change'] = (dataframe['Adj.Close'] - dataframe['Adj.Open'])/ dataframe['Adj.Open'] *100.0 

dataframe= dataframe[['Adj.Close', 'HL_PCT', 'PCT_Change', 'Adj.Volume' ]]

print(dataframe.head())