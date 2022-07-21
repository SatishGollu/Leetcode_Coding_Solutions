def gcd (n,r):
    if n == 0:
        return r
    return gcd(r%n,n)

gcd(4,2)

#combinations formula

def ncr(n,r):
    p = k = 1
    if n-r < r:
        r = n-r
    if r == 0:
        p = 1
    else:
        while r:
            p *= n
            k *= r
            gcd_value = gcd(p,k)
            p /= gcd_value
            k /= gcd_value
            n -= 1
            r -= 1
    return p/k

ncr(4,2)
ncr(12,2)
def ncr_simple(n,r):
    p = k = 1
    if n-r < r:
        r = n-r
    if r == 0:
        p = 1
    else:
        while r:
            p *= n
            k *= r
            #gcd_value = gcd(p,k)
            #p /= gcd_value
            #k /= gcd_value
            n -= 1
            r -= 1
    return p/k
ncr_simple(12,2)
