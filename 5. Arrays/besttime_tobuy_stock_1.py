def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        i,j = 0,1
        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxprofit = max(maxprofit,profit)
            else:
                i = j
            j += 1
        return maxprofit


def maxProfit(self, prices: List[int]) -> int:
    #base
    if len(prices) == 0:
        return 0
    # dp using state of machine
    s1 = -prices[0]
    s2 = float('-inf')
    for i in range(len(prices)):
        s1 = max(s1,-prices[i])
        s2 = max(s2,s1+prices[i])
    return max(0,s2)
