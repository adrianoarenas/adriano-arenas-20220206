import pandas as pd
import sys

#Reading Dataframe
df = pd.read_csv('data/trades.csv')

#combining both types of emissions
df.replace(['Emission - Venue A', 'Emission - Venue B'], 'Emissions', inplace=True)

def ohlc_resampling(df, begin, end, product, freq):
    #Turning the datetime column into the index
    df = df.set_index(pd.to_datetime(df['TradeDateTime'], infer_datetime_format=True)).drop('TradeDateTime', axis=1)
    
    #Filtering the df based on begin, end and product conditions
    condition_1 = df.index.to_series().between(begin, end, inclusive=True)
    condition_2 = df.Product == product
    
    filtered_df = df[condition_1 & condition_2]
    
    #Resampling to defined freq and grouping to get Max, Min, Open and Close
    ohlc_df = filtered_df.groupby(['Contract', pd.Grouper(freq=freq, label='left')]).\
    agg(Open = ('Price', 'first'),
        High = ('Price', 'max'),
        Low = ('Price', 'min'),
        Close = ('Price', 'last'),
        Volume = ('Quantity', 'sum')).reset_index().sort_values(['TradeDateTime', 'Contract'])

    return(ohlc_df)

if __name__ == '__main__':
    print(ohlc_resampling(df, sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
