#bitwise and
def bitand(m,n):
    count = 0
    while m!=n:
        m = m >> 1
        n = n >> 1
        count += 1
    return m << count
bitand(5,7)
bitand(0,0)
bitand(6,9)
#brian kernighan's algorithm
def biand(m,n):
    while m < n:
        #setting the right most bit to zero
        n = n & (n-1)
    return m & n
biand(5,7)
