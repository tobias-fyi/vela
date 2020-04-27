"""
Algorithms :: Practice - stock prices

You want to write a bot that will automate the task of day-trading for you
while you're going through Lambda. You decide to have your bot just focus
on buying and selling Amazon stock.

Write a function `find_max_profit` that receives as input a list of stock
prices. Your function should return the maximum profit that can be made from
a single buy and sell. You must buy first before selling; no shorting is
allowed here.
"""

import argparse
import sys


def find_max_profit(prices: list) -> int:
    """Returns the maximum profit that can be made from a single buy and sell.
    You must buy first before selling; no shorting is allowed here.
    
    :param prices (list) : List of a stock's price over some period of time.
    """
    if len(prices) < 2:  # Test if list has 2 or more items
        print(f"Cannot make a profit with only one price!")
        sys.exit(0)

    profits = []  # Empty list to hold all profits
    # Loop through list once as `buy_price`
    for buy_index, buy_price in enumerate(prices):
        # Loop through slice of list, this time as `sell_price`
        # Only the items after the current `buy_price` can be sold
        sellable_prices = prices[buy_index + 1 :]
        for sell_index, sell_price in enumerate(sellable_prices):
            # Subtract outer from inner to get profit
            current_profit = sell_price - buy_price
            profits.append(current_profit)
    # After both loops are complete, find max value in `profits`
    max_profit = profits[0]
    for i in range(len(profits) - 1):
        if profits[i] > max_profit:
            max_profit = profits[i]

    return max_profit


# amzn = [1050, 270, 1540, 3800, 2]
# print(find_max_profit(amzn))
# neg = [100, 90, 80, 50, 20, 10]
# print(find_max_profit(neg))

if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()

    print(
        f"A profit of ${find_max_profit(args.integers)} can be made from the stock prices {args.integers}."
    )

