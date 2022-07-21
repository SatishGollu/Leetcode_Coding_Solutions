#using bit manipulation trick
def hammingWeight(self, n: int) -> int:
    ssum = 0
    while n!=0:
        ssum += 1
        n = n & (n-1)
    return ssum


        


#using and mask
def hammingWeight(self, n: int) -> int:
    bits = 0
    mask = 1
    for i in range(0,32):
        if (n & mask) != 0:
            bits += 1
        mask = mask << 1
    return bits
