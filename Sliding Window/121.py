prices = [7,1,5,3,6,4]

def stockProblem(prices):
    l = 0
    r = l+1
    maxProfit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:
            l = r
        r += 1
    
    return maxProfit


res = stockProblem(prices)
print(res)

