def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #Time-O(M*N) - Space-O(M*N)
    #initiating grid of 0's with len(text2)+1 colums
    # and text1 + 1 rows
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    # iterate up each column, startng from the last one
    for col in reversed(range(len(text2))):
        for row in reversed(range(len(text1))):
            #if corresponding chars are same in this cell
            if text2[col] == text1[row]:
                dp[row][col] = 1 + dp[row+1][col+1]
            #if not they must be different
            else:
                dp[row][col] = max(dp[row + 1][col],dp[row][col+1])
    #the original answer is in dp[0][0], so we return it
    return dp[0][0]