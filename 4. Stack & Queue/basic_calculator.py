#faster one
class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        sign = 1
        num  = 0
        res = 0
        for char in s:
            if char.isdigit():
                num = num *10 + int(char)
            elif char == '+':
                res  += num *sign
                sign = 1
                num = 0
            elif char == '-':
                res += num *sign
                sign = -1
                num = 0
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                num = 0
                sign = 1
                res = 0
            elif char == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + sign * num
