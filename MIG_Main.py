"""
Created on Wed Feb 07 2024

@author: Austin Mello, Nathan Heide
"""

import pandas as pd
from MIG_Price_Scraper import scrape
from MIG_Portfolio_Analysis import *

# Load the portfolio composition.
# File must be in the same directory.
portfolio_composition = pd.read_csv('cleaned_portfolio_composition.csv')

# Ensure the 'Purchase Date' in portfolio composition is also in datetime format
portfolio_composition['Purchase Date'] = pd.to_datetime(portfolio_composition['Purchase Date'])

# Load the daily price data
daily_price_data = scrape(portfolio_composition)
#daily_price_data.to_csv('Historic_Prices.csv')

# Display the first few rows of each DataFrame to understand their structure
#print(portfolio_composition.head(), daily_price_data.head())

metrics = Portfolio_Returns(daily_price_data, portfolio_composition)
print(metrics)