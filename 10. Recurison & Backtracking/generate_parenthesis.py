#Time- 4^n/nrootn
#Space same as time
def generateParenthesis( n: int):
    stack = []
    result = []
    
    def backtrack(openN,closeN):
        if openN==closeN==n:
            result.append("".join(stack))
            
        if openN < n:
            stack.append("(")
            backtrack(openN+1,closeN)
            stack.pop()
        if closeN < openN:
            stack.append(")")
            backtrack(openN,closeN+1)
            stack.pop()
    backtrack(0,0)
    return result

if __name__ == "__main__":
    n = 3
    print(generateParenthesis(n))