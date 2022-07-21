class Solution:
    def numTrees(self, n: int) -> int:
        #using catalan numbers relationship formula
        # 2n!/(n+1)!n!
        Numerator = 2*n
        k_denominator = n+1
        result = 1
        denominator = 1
        while n > 0:
            result *= Numerator
            denominator *= k_denominator
            Numerator -=1
            k_denominator -= 1
            n -=1
        return int(result/denominator)
