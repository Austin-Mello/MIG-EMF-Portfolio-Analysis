import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

def Portfolio_Analyze(portfolio_daily_returns, iemg_daily_returns, portfolio_total_value):
    print("Calculating portfolio metrics...")
    # Define the risk-free rate (annualized)
    risk_free_rate = 0.0415

    # Number of trading days in a year
    trading_days = 252

    # Calculate annualized portfolio returns
    annualized_portfolio_returns = np.power(1 + portfolio_daily_returns.mean(), trading_days) - 1

    # Calculate portfolio volatility (annualized)
    portfolio_volatility = portfolio_daily_returns.std() * np.sqrt(trading_days)

    # Sharpe Ratio
    sharpe_ratio = (portfolio_daily_returns.mean() - risk_free_rate / trading_days) / portfolio_daily_returns.std() * np.sqrt(trading_days)

    # Sortino Ratio: using only the negative returns for downside deviation
    negative_returns = portfolio_daily_returns[portfolio_daily_returns < 0]
    sortino_ratio = (portfolio_daily_returns.mean() - risk_free_rate / trading_days) / negative_returns.std() * np.sqrt(trading_days)

    # Beta
    portfolio_returns_with_market = pd.concat([portfolio_daily_returns, iemg_daily_returns], axis=1).dropna()
    covariance = portfolio_returns_with_market.cov().iloc[0, 1]
    market_variance = portfolio_returns_with_market.iloc[:, 1].var()
    beta = covariance / market_variance

    # Alpha
    annualized_market_return = np.power(1 + iemg_daily_returns.mean(), trading_days) - 1
    alpha = annualized_portfolio_returns - (risk_free_rate + beta * (annualized_market_return - risk_free_rate))

    # Maximum Drawdown
    rolling_max = portfolio_total_value.cummax()
    daily_drawdown = portfolio_total_value / rolling_max - 1
    max_drawdown = daily_drawdown.min()

    # Cumulative Returns
    cumulative_returns = portfolio_total_value.iloc[-1] / portfolio_total_value.iloc[0] - 1

    # Value at Risk (VaR) at 95% confidence level
    var_95 = norm.ppf(1-0.95, portfolio_daily_returns.mean(), portfolio_daily_returns.std())

    # Conditional Value at Risk (CVaR) at 95% confidence level
    cvar_95 = portfolio_daily_returns[portfolio_daily_returns <= var_95].mean()

    metrics = {
        'Annualized Returns': annualized_portfolio_returns,
        'Volatility': portfolio_volatility,
        'Sharpe Ratio': sharpe_ratio,
        'Sortino Ratio': sortino_ratio,
        'Beta': beta,
        'Alpha': alpha,
        'Maximum Drawdown': max_drawdown,
        'Cumulative Returns': cumulative_returns,
        'Value at Risk (95%)': var_95,
        'Conditional Value at Risk (95%)': cvar_95
    }
    print("Done!")
    return metrics

def Portfolio_Returns(daily_price_data, portfolio_composition):
    print("Calculating portfolio returns...")
    # Calculate daily values for each equity in the portfolio
    portfolio_values = daily_price_data[portfolio_composition.index].multiply(portfolio_composition['Shares'].values, axis='columns')

    # Calculate the total daily value of the portfolio
    portfolio_total_value = portfolio_values.sum(axis=1)

    # Calculate daily returns for the portfolio
    portfolio_daily_returns = portfolio_total_value.pct_change()

    # Calculate daily returns for the IEMG index for comparison
    iemg_daily_returns = daily_price_data['IEMG'].pct_change()

    # Display the first few rows of the portfolio and IEMG daily returns for inspection
    #print(portfolio_daily_returns.head(), iemg_daily_returns.head())

    """# Plot the daily returns of the portfolio and the IEMG index
    plt.figure(figsize=(14, 7))
    plt.plot(portfolio_daily_returns, label='Portfolio Daily Returns')
    plt.plot(iemg_daily_returns, label='IEMG Daily Returns', alpha=0.75)
    plt.title('Portfolio vs. IEMG Daily Returns')
    plt.xlabel('Date')
    plt.ylabel('Daily Returns')
    plt.legend()
    plt.grid(True)
    plt.show()"""

    print("Done!")
    return Portfolio_Analyze(portfolio_daily_returns, iemg_daily_returns, portfolio_total_value)