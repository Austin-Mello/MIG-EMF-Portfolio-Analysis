"""
Created on Wed Feb 07 2024

@author: Austin Mello, Nathan Heide
"""

import pandas as pd
from datetime import date
from MIG_Price_Scraper import scrape
from MIG_Portfolio_Analysis import *
import csv

# Load the portfolio composition.
# File must be in the same directory.
portfolio_composition = pd.read_csv('cleaned_portfolio_composition.csv')

# Ensure the the dates in portfolio composition is also in datetime format
# If the end date is empty, use today's date
portfolio_composition['Purchase Date'] = pd.to_datetime(portfolio_composition['Purchase Date'])
portfolio_composition['Sell Date'] = pd.to_datetime(portfolio_composition['Sell Date'])
today = date.today().strftime("%m/%d/%Y")
portfolio_composition['Sell Date'] = portfolio_composition['Sell Date'].fillna(date.today().strftime("%m/%d/%Y"))

print(portfolio_composition)

# Load the daily price data.
daily_price_data = scrape(portfolio_composition)
#daily_price_data.to_csv('Historic_Prices.csv')

# Run analyses on the historic price data.
metrics = Portfolio_Returns(daily_price_data, portfolio_composition)
print(metrics)