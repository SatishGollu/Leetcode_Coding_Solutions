#segment tree implementation
seg_arr = []

def buildSegTree(st_index,arr,start,end):
    #base case
    if start > end :
        return
    #if we reach last leaf node
    if start == end:
        st[st_index] = arr[start]
        return
    #if it is not a leaf node--> internal node
    mid = start + (end-start)//2
    buildSegTree(2*st_index,arr,start,mid)
    buildSegTree(2*st_index+1,arr,mid+1,end)
    st[st_index] = st[2*st_index] + st[2*st_index+1]
def query(qs,qe,st_index,start,end):
    #no overlap
    if qs > end or qe < start:
        return 0
    #total overlap
    if start >= qs and end <= qe:
        return st[st_index]
    #partial overlap
    mid = start + (end-start)//2
    leftsum = query(qs,qe,2*st_index,start,mid)
    rightsum = query(qs,qe,2*st_index+1,mid+1,end)
    return leftsum + rightsum
#updating node
def UpdateNode(st_index,start,end,pos,newvalue):
    #no overlap
    if start > pos or end < pos:
        return 
    #total overlap
    if start == end:
        st[st_index] = newvalue
        return
    #internal node--> partial overlap
    mid = start + (end-start)//2
    UpdateNode(2*st_index,start,mid,pos,newvalue)
    UpdateNode(2*st_index+1,mid+1,end,pos,newvalue)
    st[st_index] = st[2*st_index] + st[2*st_index+1]    

if __name__ == '__main__':
    n = 6
    arr = [1,3,2,-2,4,5]
    st = [0]*(4*n+1)
    st_index = 1
    start,end = 0,n-1

    #preprocess and build segment tree
    buildSegTree(st_index,arr,start,end)
    print(st)#printing the segment tree
    #range query
    print(query(2,4,st_index,start,end))
    print(query(3,3,st_index,start,end))

    #update node
    arr[2] = 999
    UpdateNode(st_index,start,end,2,999)
    print(st)
    



