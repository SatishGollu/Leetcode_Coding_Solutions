class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_close  = {"(":")","{":"}","[":"]"}
        open_ = set(["(","[","{"])
        for each in s:
            if each in open_:
                stack.append(each)
            elif stack and each == open_to_close[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []

        
