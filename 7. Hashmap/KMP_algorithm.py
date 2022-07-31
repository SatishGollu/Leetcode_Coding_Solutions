def strStr(self, haystack: str, needle: str) -> int:
    #implementing knutt-morris-pratt algorithm- Time(n+m)
    def longestPrexSufx(n):
        lps = [0]*len(n)
        i,j= 0,1 #pointers to traverse
        while j < len(n):
            if n[j] == n[i]:
                lps[j] = i + 1
                j += 1
                i += 1
            
            elif i == 0:
                lps[j] = 0
                j += 1
            else:      
                i = lps[i-1]
        return lps
    #main kmp
    if needle == "": return 0
    i = 0 #pointer for haystack
    j = 0 #pointer for needle
    lps = longestPrexSufx(needle)
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j == 0: # if there is nothing to compare
                i += 1
            else:
                j = lps[j-1]
        #if j equal to length return 
        if j == len(needle):
            return i-len(needle)
    return -1
        
    
                
        
    
    
    
    
    
    
    
    '''
    #implemnting brute force
    #Time - O(n*m) - lengths of needle and haystack
    h = len(haystack)
    n = len(needle)
    for i in range(h-n+1):
        if needle == haystack[i:i+n]:
            return i
    return -1
    
    '''