# optimaization O(n2)
#Space O(n2)
def generate(numRows):
        result = [[1]]
        #base condition
        if numRows == 0: return 0
        if numRows == 1: return result
        for i in range(1,numRows):
            temp = [1]*(len(result[-1])+1)
            for j in range(1,i):
                temp[j] = result[-1][j-1] + result[-1][j]
            result.append(temp)
        return result
            
        