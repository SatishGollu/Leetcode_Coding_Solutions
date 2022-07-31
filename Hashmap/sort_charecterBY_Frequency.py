# brute force O(n2)
def frequencySort(self, s: str) -> str:
    #using hashmap to count frequencies -- sort- and add in reverse
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char,0)+1
    #sort the hashmap
    char_count = sorted(char_count.items(),key=lambda x:x[1])
    result = ""
    for i in range(len(char_count)-1,-1,-1):
        for j in range(char_count[i][1]):
            result += char_count[i][0]#this will O(n2)
    return result

# optimized one
def frequencySort(self, s: str) -> str:
    #using hashmap to count frequencies -- sort- and add in reverse
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char,0)+1
    #sort the hashmap
    char_count = sorted(char_count.items(),key=lambda x:x[1],reverse = True)
    result = []
    for char,freq in char_count:
        result.append(char*freq)
    return "".join(result)

# using multiset and bucket sort
# TIme - O(N) -- Space O(N)
