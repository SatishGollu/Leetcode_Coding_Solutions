
#to check if its a prime number
#time - O(n)
def prime_v1(n):
    count = 0
    i = 1
    while i <= n:
        if n%i == 0:
            count +=1
        i +=1
    if count ==2:
        print('yes')
    else: print('No')
prime_v1(7)

#optimized time - O(sqrt(n))
def prime_v2(n):
    count = 0
    i = 1
    while i*i < n:
        if n%i == 0:
            count +=1
            if n/i !=i:
                count +=1
        i +=1
    if count ==2:
        print('yes')
    else: print('No')
prime_v2(36)


#print the sum of factors
def sum_factors(n):
    sum = 0
    i = 1
    while i * i < n:
        if n%i == 0:
            sum += i
            if n/i != i:
                sum += n/i
        i +=1
    return sum

sum_factors(3)
#print kth factore
#brute force
def factors(n,k):
    i = 1
    result = []
    while i <= n:
        if n%i ==0:
            result.append(i)
        i +=1
    if len(result) <= k:
        return -1
    return result[k-1]
factors(4,4)

#optimized
def kthfact(n,k):
    divisors = []

    for i in range(1, int(n**5)+1):
        if n%i == 0:
            k -=1

n=36
i = 1
result = []
while i <= n:
    if n%i ==0:
        result.append(i)
    i +=1

result


4*(4-1)/2






#
