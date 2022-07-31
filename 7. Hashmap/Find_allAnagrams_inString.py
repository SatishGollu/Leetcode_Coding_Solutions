def findAnagrams( s, p):
    # Using lists 
    sl = len(s)
    pl = len(p)
    if pl > sl: return []
    scount,pcount = [0]*26,[0]*26
    #counting the frequency in the string p
    for i in p:
        pcount[ord(i)-ord('a')] += 1
    #applying sliding window technique on string s and compare with p
    result = []
    for i in range(sl):
        scount[ord(s[i])-ord('a')] += 1
        #remove one letter form left side of window
        if i >= pl:
            scount[ord(s[i-pl]) - ord('a')] -= 1
        if pcount == scount:
            result.append(i-pl+1)
    return result
                
                   
        
'''
    Time complexity: O(Ns)

    We perform one pass along each string when Ns≥Np which costs O(Ns+Np)time. 
    Since we only perform this step when Ns≥Np the time complexity simplifies to O(Ns)

    Space complexity: O(K)

    pCount and sCount contain K elements each. Since K is fixed at 26 for this problem,
    this can be considered as O(1) space.
'''
        