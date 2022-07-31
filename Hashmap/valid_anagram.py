# Time - O(nlogn), Space - O(n)
def isAnagram(self, s, t):
    return sorted(s) == sorted(t)

# time - O(n), space - O(m) m is size of alphabet
#  using counter
import collections
def isAnagram(self, s: str, t: str) -> bool:
        #brute force
        return collections.Counter(s) == collections.Counter(t)
#same above complexity coding in regular way
def isAnagram(self, s: str, t: str) -> bool:
        d1,d2 = {},{}
        for char in s:
            d1[char] = d1.get(char,0)+1
        for char in t:
            d2[char] = d2.get(char,0)+1
        return d1 == d2
