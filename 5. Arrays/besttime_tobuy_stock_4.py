def maxProfit(self, k: int, prices: List[int]) -> int:
        #base case
        if len(prices) == 0:
            return 0
        #base case 2
        if k <= 0:
            return 0

        # dp using state machine with k transactions
        states = [0] + [-float('inf') for x in range(2*k)]

        states[1] = -prices[0]

        for i in range(1,len(prices)):
            for j in range(k):
                states[2*j+1] = max(states[2*j+1], states[2*j]-prices[i])
                states[2*j+2] = max(states[2*j+2], states[2*j+1]+prices[i])
        return max(0,states[-1])
        
