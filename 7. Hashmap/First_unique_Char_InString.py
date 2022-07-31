#using hashmap with Time--O(n)
def firstUniqChar(self, s: str) -> int:
        #using hashmap count the frequencies
        hashmap = {}
        for charr in s:
            hashmap[charr] = hashmap.get(charr,0)+1
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1

# can also use frequencies of 26 abcd charters
def firstUniqChar(self, s: str) -> int:
    #using
    freq = [0] * 26
    #if we increase size to 256 then it is enough for any character
    for i in s:
        freq[ord(i) - ord('a')] += 1
    for index,charr in enumerate(s):
        if freq[ord(charr) - ord('a')] == 1:
            return index
    return -1
#after multiple submits using hashmap has less runtime compared to list