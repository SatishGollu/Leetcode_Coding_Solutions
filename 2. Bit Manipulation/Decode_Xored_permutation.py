#first let's learn about xored array decoding
    """
According to Xor property

The inverse is XOR!

If you have:
c = a^b;
You can get a or b back if you have the other value available:
a = c^b; // or b^c (order is not important)
b = c^a; // or a^c

encoded[i] = arr[i] ^ arr[i+1]

Here we have an encoded array, and we want a resultant array, so we can interchange

res[0] = first
res[i+1] = res[i] ^ encoded[i]
    """

def decode(encoded, first):

        result = [first]
        for each in encoded:
            result.append(result[-1]^each)
        return result
#now for the original question if we can find the first element
#then we can compute easily

def first_element(n):
    and_n = n & (n-1)
    result = and_n ^ n
    return result if result > and_n else and_n
first_element(7)
first_element(3)
first_element(6)


def decode(n):
    first_elmnt = n[0] & (n[0]-1) ^ n[0]
    result = [first_elmnt]
    for each in n:
        result.append(result[-1]^each)
    return result

encoded = [6,5,4,6]
decode(encoded)



#
