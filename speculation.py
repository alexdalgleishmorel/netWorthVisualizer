import globals as globals
import pathlib
import yfinance

def calculateAverageCost(asset, cash):

    sharesToBuy = ((cash-10)/(asset.currentPrice))

    # Returning the new average cost if the user put in the given amount of cash
    return ((asset.averageCost*asset.shares)+(asset.currentPrice*sharesToBuy))/(asset.shares+sharesToBuy)

def convertEthereum(asset):
    ticker = yfinance.Ticker("ETH-USD")
    data = ticker.history()
    return (data.tail(1)['Close'].iloc[0])/asset.currentPrice

def convertBitcoin(asset):
    ticker = yfinance.Ticker("BTC-USD")
    data = ticker.history()
    return (data.tail(1)['Close'].iloc[0])/asset.currentPrice
