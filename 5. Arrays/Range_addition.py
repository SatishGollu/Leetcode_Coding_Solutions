def getModifiedArray(length, updates):
        #brute force-Time limit exceeded
        #array to store the result
        arr = [0] * length
        for each in updates:
            for i in range(each[0],each[1]+1):
                arr[i] += each[2]
        return arr
# optimization
#Time complexity : O(n+k)O(n + k)O(n+k). Each of the k update
# operations is done in constant O(1) time. 
# The final cumulative sum transformation takes 
# O(n) time always.
def getModifiedArray(length, updates):
        #brute forcce-Time limit exceeded
        #array to store the result
        arr = [0] * length
        for start,end,val in updates:
            arr[start] += val
            if end+1 < length:
                arr[end +1] -= val
        #changing to it's original form
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
        return arr
        