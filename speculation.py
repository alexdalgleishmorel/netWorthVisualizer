import globals as globals
import pathlib

"""
def prospectAverageCost (asset, targetAverageCost, targetStockPrice):

    priceRange = 2

    startPrice = asset.currentPrice-(priceRange/2)

    print("current average cost: {0}".format(asset.averageCost))
    print("current book value: {0}".format(asset.bookValue))
    print("current shares: {0}".format(asset.shares))

    while (startPrice <= asset.currentPrice):

        sharesToPurchase = ((startPrice*asset.shares)-asset.bookValue)/(asset.currentPrice-startPrice)
        resultingCost = sharesToPurchase*asset.currentPrice

        print("Target average cost --> {0}".format(startPrice))
        print("Shares to purchase: {0:.2f} with resulting cost of: {1:.2f}".format(sharesToPurchase, resultingCost))
        print()

        startPrice += 0.1

"""

def calculateAverageCost(asset, cash):

    sharesToBuy = ((cash-10)/(asset.currentPrice))

    # Returning the new average cost if the user put in the given amount of cash
    return ((asset.averageCost*asset.shares)+(asset.currentPrice*sharesToBuy))/(asset.shares+sharesToBuy)