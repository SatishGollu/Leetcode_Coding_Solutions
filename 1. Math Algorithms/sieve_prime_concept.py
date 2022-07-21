#gcd
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)
gcd(20,30)
int(10**.5)+1
#implementing the sieve of eratosthenes
#let's implement for 25 numbers
#pythonic version
def create_sieve(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2,int(n**0.5)+1):
        if primes[i] == True:
            primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
    return primes
create_sieve(15)

#regular way
def create_sieve(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2,int(n**0.5)+1):
        if primes[i] == True:
            for j in range(i*i,n):
                primes[j] = False
    return primes

create_sieve(5)


#kth prime number
def kth_prime(k):
    n = 100000
    box = create_sieve(n)
    store = []
    for i in range(len(box)):
        if box[i] == True:
            store.append(i)
    return store[k-1]
    #from above result we can print kth prime
    #by indexing k-1 bcoz index starts with 0

kth_prime(100)

#prime_factorization

#brute force
def p_factor(n):
    result = []
    for i in range(2,n):
        while n%i == 0:
            result.append(i)
            n = n/i
    return result
p_factor(48)



#optimised version -O(sqrt(n))
#using square root and adding condition
def prime_factors(n):
    result = []
    for i in range(2,int(n**0.5)+1):
        while n%i == 0:
            result.append(i)
            n = n/i
    if n > 1:
        result.append(int(n))
    return result

prime_factors(35)


"""the above will still not that optimal if n is at 10^6  then the
the time complexity will by n*sqrt(n)..so by using seive we can still
reduce the complexity
"""

#Create a sieve with numbers itself and multiple will be replaced
#with its smallest factor

def sieve_nums(n):
    box = []
    for i in range(n):
        box.append(i)
    for i in range(2,int(n**0.5)):
        if box[i] == i:
            for j in range(i*i,n):
                if box[j] == j:
                    box[j] = i
                j+=i



    return box


sieve_nums(10)





#












#
