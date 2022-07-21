#my trail using or and counting set bits

def hamming(x,y):
    #my method -O(1)-time
        res = x^y
        count = 0
        while res != 0:
            count += 1
            res = res & (res-1)
        return count

hamming(1,4)
hamming(3,1)
'''
#built-in
return bin(x^y).count('1')
'''
