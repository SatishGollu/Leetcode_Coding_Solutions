def maxProfit(self, prices: List[int]) -> int:
        #base condition
        if len(prices) == 0:
            return 0
        # Dp using state machine
        #We begin at state 0, where we can either rest (i.e. do nothing) or buy stock at a given price.
        #If we choose to rest, we remain in state 0
        #If we buy, we spend some money (price of the stock on that day) and go to state 1
        s1 = -prices[0]
        #From state 1, we can once again choose to do nothing or we can sell our stock.
        #If we choose to rest, we remain in state 1
        #If we sell, we earn some money (price of the stock on that day) and go to state 2
        s2 = float('-inf')
        #This completes one transaction for us. Remember, we can only do atmost 2 transactions.

        #From state 2, we can choose to do nothing or buy more stock.
        #If we choose to rest, we remain in state 2
        #If we buy, we go to state 3
        s3 = float('-inf')
        #From state 3, we can once again choose to do nothing or sell our stock for the last time.
        #If we choose to rest, we remain in state 3
        #If we sell, we have utilized our allowed transactions and reach the final state 4
        s4 = float('-inf')

        #iterate for all prices and update
        for i in range(1,len(prices)):
            s1 = max(s1,-prices[i])
            s2 = max(s2,s1+prices[i])
            s3 = max(s3,s2-prices[i])
            s4 = max(s4,s3+prices[i])

        return max(0,s4)

        
