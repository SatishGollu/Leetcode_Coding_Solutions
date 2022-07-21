
#How to check N --> Prime
def check_prime(N):
    for i in range(2,int(N**0.5)+1):
        if N%i ==0:
            return "Not Prime"
    return "Yes it's Prime"

check_prime(10)
check_prime(7)
check_prime(2)


#2 Factors exists in pairs
def factors(n):
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            print(i,",",int(n/i))
factors(36)

#3 Find primes from 2 to N
def prime_numbers(n):
    for i in range(2,n):
        for j in range(2,int(n**0.5)+1):
            if i%j ==0:
                return 'Not prime'
    return "It's Prime"
prime_numbers(10)


#decimal to binary
def dectoB(val):
    if val > 1:
        dectoB(val//2)
    print(val % 2,end = '')

dectoB(7)

def test(val):
    while val>=1:
        val = val//2
        print(val%2,end = '')

test(7)
n= [1,2,3,1,1,3]

#identical pairs

def pairs(nums):
    hash = {}
    count = 0
    for i in nums:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    for key,val in hash.items():
        if val > 1:
            count += val*(val-1)/2
    return int(count)


nums = [1,2,3,1,1,3,4]
pairs(nums)

dic = {1:3,2:7,3:2}
for k,v in dic.items():
    print(k,v)

nums.count(1)
hash = {}
for i in nums:
    hash[i] = nums.count(i)


hash

# ncr = n(n-1)/2






















#
