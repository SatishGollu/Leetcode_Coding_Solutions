class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.ans = set()
        self.min_removed = float("inf")
        
        def dfs(depth, left,right,removed,cur):
            #base
            if depth == len(s):
                if left == right:
                    if removed < self.min_removed:
                        self.min_removed = removed
                        self.ans = {cur}
                    elif removed == self.min_removed:
                        self.ans.add(cur)
            else:
                if s[depth] != "(" and s[depth] != ")":
                    dfs(depth +1,left,right,removed,cur+s[depth])
                else:
                    dfs(depth+1,left,right,removed+1,cur)
                    if s[depth] == "(":
                        dfs(depth +1,left+1,right,removed,cur + "(")
                    elif s[depth] ==")" and right < left:
                        dfs(depth + 1, left,right+1,removed,cur + ")")
        dfs(0,0,0,0,"")
        return list(self.ans)

class Solution: # optimized one
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = right = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left == 0:
                    right += 1
                else:
                    left -= 1

        def dfs(depth, left, right, left_rem, right_rem, cur):
            if depth == len(s):
                if left == right and left_rem == right_rem == 0:
                    self.ans.add(cur)
                    return
            else:  # s[depth] can only be either a left paren, right paren or a letter
                if s[depth] == "(":
                    if left_rem > 0:   # if we can remove a left paren
                        dfs(depth + 1, left, right, left_rem - 1, right_rem, cur)
                    dfs(depth + 1, left + 1, right, left_rem, right_rem, cur + "(")  # keep current left paren
                elif s[depth] == ")":
                    if right_rem > 0:  # if we can remove a right paren
                        dfs(depth + 1, left, right, left_rem, right_rem - 1, cur)
                    if left > right:  # if we can keep the right paren, see LC 22. Generate Parentheses
                        dfs(depth + 1, left, right + 1, left_rem, right_rem, cur + ")")
                else:  
                    dfs(depth + 1, left, right, left_rem, right_rem, cur + s[depth])  # we must keep the letter

        self.ans = set()
        dfs(0, 0, 0, left, right, "")
        return list(self.ans)