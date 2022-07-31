#Time- O(m*n*26) ~ O(mn)
#space - O(mn)
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    result = defaultdict(list)
    for each in strs:
        count = [0]*26 # a ....z
        
        for char in each:
            count[ord(char) - ord("a")] += 1
        result[tuple(count)].append(each)
    return result.values()

#using sorted function
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    result = {}
    for each in strs:
        #sorting the each word
        sortedwd = ''.join(sorted(each))
        if sortedwd not in result:
            result[sortedwd] = [each]
        else:
            result[sortedwd].append(each)
    return result.values()
    