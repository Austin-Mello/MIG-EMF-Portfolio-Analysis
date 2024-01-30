#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 2024

@author: Austin Mello
"""

from yahoo_fin.stock_info import get_data
from datetime import date
import pandas as pd

today = date.today()

# This table holds the liast of tickers for our current holdings.
tickerList = ['ASAI','TSM','LPL','KT','PKX','FN','NTES','SQM','YNDX','ANPDY',
              'MMYT','AU','TCEHY','JD','WNS','GRVY','PAGS','EBR','NIO','RDY',
              'YUMC','PBR','TME','WIT','TGLS']

# This table holds the corresponding purchase date for each of the holdings
startList = ['3/8/2021','2/22/2013','2/19/2015','2/4/2016','4/15/2016',
             '11/21/2016','12/8/16','5/11/17','5/25/17','5/25/18','6/8/17',
             '4/7/21','11/30/17','11/30/17','1/25/18','2/27/2019','3/21/2019',
             '1/21/2021','2/1/2022','2/1/2022','2/10/2022','2/28/2022',
             '5/6/2021','2/23/2023','3/13/2023',]

#Today's date
end = today.strftime("%m/%d/%Y")

#Dataframe for the holdings
prices = pd.DataFrame()

""" Calls Yahoo Finance's API for the info on each element of the ticker list,
    rips out the daily closing prices for each of the tickers, and stores it
    in the "prices" dataframe. """
for i in range(len(tickerList)):
    ticker = get_data(tickerList[i],start_date=startList[i], end_date=end)
    prices[tickerList[i]] = ticker.close

# Stores the dataframe in a csv file. Look inside whatever folder you put 
#    this file in. It should be there.
prices.to_csv('Historic_Prices.csv')