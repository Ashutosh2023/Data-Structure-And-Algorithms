#Best time to buy and sell stock:
def buySellStock(prices: list[int]) -> int:
    n = len(prices)
    maxDiff = 0
    for i in range(n):
        for j in range(i, n):
            diff = prices[j]-prices[i]
            maxDiff = max(diff, maxDiff)
    return maxDiff


prices = [7,6,4,3,1]
# print(buySellStock(prices))


def buySellStock2(prices: list[int]) -> int:
    minPrice = 2**31 -1
    maxProfit = 0

    for price in prices:
        if price < minPrice:
            minPrice = price
        profit = price - minPrice
        if profit > maxProfit:
            maxProfit = profit
    return maxProfit


prices = [7,6,4,3,1]
print(buySellStock2(prices))