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

#using heap
# Time O(nlogk)
#space O(n)
class Solution: 
    import heapq
    def frequencySort(self, s: str) -> str:
        #using heap-- Time- O(nlogk), Space-O(n)
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        heap = []
        for key in char_count:
            heapq.heappush(heap,(-char_count[key],key))
        
        result = []
        for _ in range(len(char_count)):
            popped_element = heapq.heappop(heap)
            result.append((-1*popped_element[0])*popped_element[1])
        return "".join(result)

# using multiset and bucket sort
# TIme - O(N) -- Space O(N)
class Solution: 
    def frequencySort(self, s: str) -> str:
    
        #using bucket sort
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        #frequency array
        freq = [[] for _ in range(len(s)+1)]
        #now add values to the corresponding freq
        for char,count in char_count.items():
            freq[count].append(char)
        result = []
        for each in range(len(freq)-1,-1,-1):
            for i in freq[each]:
                result.append(i*each)
        return "".join(result)  

#surprisingly using heap gave faster results
#run time is less compared to O(N) algorithm

