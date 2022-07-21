# 
#optimized
def myPow(self, x: float, n: int) -> float:

    #creating
    result = 1
    a = x
    b = abs(n)
    while b > 0:
        if b%2 == 1:
            result *= a
        a *= a
        b //= 2
    if n < 0:
        return 1/result
    return result

#brute force
def pow(x,n):
    result = 1
    i = 0
    while i < n:
        result = result*x
        i +=1
    return result
pow(2,10)
