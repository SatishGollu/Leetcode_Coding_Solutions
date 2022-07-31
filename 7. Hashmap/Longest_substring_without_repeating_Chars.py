def length_of_lonest_substring(s):
    #Time-O(N),Space O(N)
    #taking a set()
    charset = set()
    left = 0
    result = 0
    for right in range(len(s)):
        while s[right] in charset:
             charset.remove(s[left])
             left += 1
        charset.add(s[right])
        result = max(result, right-left+1)
    return result