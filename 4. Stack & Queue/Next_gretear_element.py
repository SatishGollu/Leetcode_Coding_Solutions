#next greater element

arr = [13,7,6,12,10]
#brute force/naive approach
def brute_NGE(arr):
    n = len(arr)
    for i in range(0,n):
        next = -1
        for j in range(i+1,n):
            if arr[i] < arr[j]:
                next = arr[j]
                break
        print(next)
brute_NGE(arr)

#my way of coding
def next_GE(arr):
    n = len(arr)
    indx = {n:i for i,n in enumerate(arr)}
    result = [-1] * n
    stack = []
    stack.append(arr[0])
    for i in range(1,n):
        curr = arr[i]
        while stack and curr > stack[-1]:
            pop_ele = stack.pop()
            index = indx[pop_ele]
            result[index] = curr
        stack.append(curr)
    return result

next_GE(arr)
t2 = [4,5,2,25]
next_GE(t2)
tcase = [11,13,21,3]
t2 = [6,8,0,1,3]
my_NGE(t2)

t3 = [4,5,2,25]
my_NGE(t3)



#
