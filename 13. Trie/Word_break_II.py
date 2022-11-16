from collections import defaultdict
class recursive_memo:
    #top-down dp with recursion
    #time- O(N^2+2^N+W)
    #Space - O(2^N.N + W)
    def wordBreak( s, wordDict) :
        word_set = set(wordDict)
        memo = defaultdict(list)
        def wb_topdown(s):
            #base
            if len(s) == 0:
                return [[]]
            if s in memo:
                return memo[s]
            for end in range(1,len(s)+1):
                word = s[:end]
                if word in word_set:
                    for each in wb_topdown(s[end:]):
                        memo[s].append([word]+each)
            return memo[s]
        wb_topdown(s)
        return [" ".join(word) for word in memo[s]]

