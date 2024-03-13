#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 2024

@author: Austin Mello
"""

from yahoo_fin.stock_info import get_data
from datetime import date
import pandas as pd

def scrape(portfolio):
    print("Scraping the web for price data...")
    portfolio.set_index('Equity', inplace=True)
    portfolio = portfolio.sort_values(by='Purchase Date')

    #Dataframe for the holdings
    prices = pd.DataFrame()

    #Grab timestamps
    today = date.today()
    start = portfolio['Purchase Date'][0]
    end = today.strftime("%m/%d/%Y")

    #Query API for benchmark data.
    prices['IEMG'] = get_data('IEMG', start_date=start, end_date=end).close

    """Calls Yahoo Finance's API for the info on each element of the ticker list,
        rips out the daily closing prices for each of the tickers, and stores it
        in the "prices" dataframe. If you can think of a more elegant way to do 
        this, do it yourself."""
    for i, row in portfolio.iterrows():
        prices[i] = get_data(i,start_date=row[2], end_date=row[3]).close


    print("Done!")
    return prices