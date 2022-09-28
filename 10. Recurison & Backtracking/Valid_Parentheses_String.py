class Using_Stack_Solution:
    def checkValidString(self, s: str) -> bool:
        #using stack - Time-O(n),space-O(n)
        openstack = []
        starstack = []
        if s[0] == ')':
            return False
        
        for i in range(len(s)):
            if s[i] == '(':
                openstack.append(i)
            elif s[i] == '*':
                starstack.append(i)    
            else:
                if openstack:
                    openstack.pop()
                elif starstack:
                    starstack.pop()
                else:
                    return False
        #balancing closed braces
        while openstack:
            if not starstack: return False
            elif openstack[-1] < starstack[-1]:
                openstack.pop()
                starstack.pop()
            else:return False
        return True #len(openstack) == 0
class greedy_Solution:
    def checkValidString(self, s: str) -> bool:
        #using greedy method
        # time -O(N), Space - O(1)
        low = high = 0
        for c in s:
            if c == '(':
                low += 1
            else:
                low -= 1
            if c != ')':
                high += 1
            else:
                high -= 1
            if high < 0:
                return False
            low = max(low,0)
        return low == 0
               