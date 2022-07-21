#time-O(n),space-O(n)
def maxProfit(self, prices: List[int]) -> int:
        #size of the given prices
        n = len(prices)
        # there are only 1 or fewer days to trade stocks, so we cannot make a profit
        # by buying or selling, so we don't buy or sell
        if n <= 1:
            return 0
        #intializing 3 lists to store the values
        no_stock,in_hand,sold = [0]*n,[0]*n,[0]*n
        no_stock[0] = 0
        in_hand[0] = -prices[0]
        sold[0] = 0

        for i in range(1,n):
            no_stock[i] = max(no_stock[i-1],sold[i-1])
            in_hand[i] = max(in_hand[i-1],no_stock[i-1]-prices[i])
            sold[i] = in_hand[i-1] + prices[i]
        return max(no_stock[n-1],sold[n-1])

#little optimization
#Time-O(n)
#Space -O(1)-dp sliding window and state of machine
def maxProfit(self, prices: List[int]) -> int:
        #size of the given prices
        n = len(prices)
        # there are only 1 or fewer days to trade stocks, so we cannot make a profit
        # by buying or selling, so we don't buy or sell
        if n <= 1:
            return 0
        #These variable will be used to implement the DP Sliding Window Technique

        prev_no_stock = 0
        # Here we buy a stock on the very first day and have not sold it, yet
        prev_in_hand= -prices[0]
        prev_sold = 0

        for i in range(1,n):
            # We have no stock today if we:
            # 1. Had no stock yesterday also, and we didn't do anything about it
            # 2. We sold a stock yesterday
            curr_no_stock = max(prev_no_stock,prev_sold)
            # We have a stock in hand today if we:
            # 1. Had a stock in hand yesterday as well, and we didn't do anything about it
            # 2. Had no stock yesterday but we bought a stock today
            curr_in_hand = max(prev_in_hand,prev_no_stock-prices[i]) #// We subtract prices[i] as we bought a stock
            #We have sold a stock today, if we:
            # Only had a stock in hand yesterday and we sold it today
            curr_sold = prev_in_hand + prices[i]#We add prices[i] as we sold a stock

            prev_no_stock = curr_no_stock
            prev_in_hand = curr_in_hand
            prev_sold = curr_sold


        return max(curr_no_stock,curr_sold)
