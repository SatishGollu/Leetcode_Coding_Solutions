
#how can we print range of numbers set bit count
#O(nlogn)
def ones_count(n):
    def popcount(n):
        count = 0
        while n!=0:
            count += 1
            n = n & (n-1)
        return count
    result = [0]* (n+1)
    for i in range(n+1):
        result[i] = popcount(i)
    return result

ones_count(5)

#o(n) time - dp plus least significant bit
def count_bits(n):
    ans = [0] * (n+1)
    for each in range(1,n+1):
        ans[each] = ans[each >> 1] + (each & 1)
    return ans

count_bits(5)

# O(n) last set bit +dp
def countBits(self, n: int) -> List[int]:
    ans = [0] * (n+1)
    for each in range(1,n+1):
        ans[each] = ans[each & (each-1)] + 1
    return ans
#















#for a single number
def set_bit_count(n):
    count = 0
    while n != 0:
        if n & 1 == 1:
            count +=1
        n = n >> 1
    return count
set_bit_count(7)

#using bit manipulation trick
def countbit(n):
    count = 0
    while n!=0:
        count += 1
        n = n & (n-1)
    return count

countbit(7)
