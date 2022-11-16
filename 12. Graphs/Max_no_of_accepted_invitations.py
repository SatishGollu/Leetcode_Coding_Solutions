#Hungarian Solution
class Solution:
    def maximumInvitations(self, grid):
        M = len(grid)
        N = len(grid[0])
        matching = [-1]* N # girls mate

        def dfs(boy,visited):
            #ask each girl
            for girl in range(N):
                # a potential mate, the girl has not been asked before
                if grid[boy][girl] and girl not in visited:
                    #mark her as asked
                    visited.add(girl)
                    #if the girl does not have a mate or
                    #her mate can be matched to someone else
                    if matching[girl] == -1 or dfs(matching[girl], visited):
                        matching[girl] = boy
                        return True
            return False
        for boy in range(M):
            dfs(boy,set())
        
        result = 0
        for i in matching:
            if i != -1:
                result += 1
        return result


