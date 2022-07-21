#finding the exact row
# Time- O(k)
def getRow(rowIndex):
        row = [1] * (rowIndex+1)
        n = rowIndex
        r = 1
        for i in range(1,rowIndex):
            row[i] = round((row[i-1]*n)/r)
            n -= 1
            r += 1
        return row