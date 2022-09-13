def flatten(root):
#Your code here
    #base
    if not root or not root.next:
        return root
    #for list on the right
    root.next = dfs(root.next)
    #merge
    root =  mergelist(root,root.next)
    return root
    
def mergelist(x,y):
    if x is None:
        return y
    if y is None:
        return x
    # value
    temp = Node(0)
    result = temp
    while x and y:
        if x.data < y.data:
            temp.bottom = x
            temp = temp.bottom
            a = a.bottom
        else:
            temp.bottom = y
            temp = temp.bottom
            b = b.bottom
    if x:
        temp.bottom = x
    if y:
        temp.bottom = y
    return result.bottom



'''
Time Complexity: O(N * N * M)  where N is the no of nodes in the main
 linked list and M is the no of nodes in a single sub-linked list 
Explanation: As we are merging 2 lists at a time,

After adding the first 2 lists, the time taken will be O(M+M) = O(2M).
Then we will merge another list to above merged list -> time = O(2M + M) = O(3M).
Then we will merge another list -> time = O(3M + M).
We will keep merging lists to previously merged lists until all lists are merged.
Total time taken will be O(2M + 3M + 4M + …. N*M) = (2 + 3 + 4 + … + N) * M
Using arithmetic sum formula: time = O((N * N + N -2) * M/2)
The above expression is roughly equal to O(N * N * M) for a large value of N

Auxiliary Space: O(N*M)- because of the recursion. The recursive functions will use a recursive stack of a size equivalent to a total number of elements in the lists, which is N*M.
'''