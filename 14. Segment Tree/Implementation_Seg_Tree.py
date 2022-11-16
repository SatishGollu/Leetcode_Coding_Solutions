class Segment_Tree:

    def build_Seg_Tree(seg_array,st_index,arr,start,end):
        #base
        if start > end:
            return

        # if we reach last leaf node
        if start == end:
            seg_array[st_index] = arr[start]
            return
        # if it's not a leaf node
        mid = start + (end-start)//2
        build_Seg_Tree(seg_array,2*st_index,arr,start,mid)
        build_Seg_Tree(seg_array,2*st_index+1,arr,mid+1,end)
        seg_array[st_index] = seg_array[2*st_index] + seg_array[2*st_index+1]

    def query(seg_array,st_index,qs,qe,start,end):
        #no overlap
        if qs > end or qe < start:
            return 0
        #total overlap
        if start >= qs and end <= qe:
            return seg_array[st_index]
        #partial overlap
        mid = start + (end-start)//2
        leftsum = query(seg_array,2*st_index,qs,qe,start,mid)
        rightsum = query(seg_array,2*st_index+1,qs,qe,mid+1,end)
        return leftsum + rightsum
    def updateNode(seg_array,st_index,start,end,pos,new_value):
        # no overlap
        if start > pos or end < pos:
            return
        # total overlap
        if start == end:
            seg_array[st_index] = new_value
            return
        mid = start + (end-start)//2
        updateNode(seg_array,2*st_index,start,mid,pos,new_value)
        updateNode(seg_array,2*st_index+1,mid+1,end,pos,new_value)
        seg_array[st_index] = seg_array[2*st_index] + seg_array[2*st_index+1]

if __name__ == '__main__':
    arr = [1,3,2,-2,4,5]
    n = len(arr)
    seg_array = [0] *(4*n+1)
    st_index = 1
    start = 0
    end = n-1
    build_Seg_Tree(seg_array,st_index,arr,start,end)
    print(seg_array)
    print(query(seg_array,st_index,2,4,start,end))
    #update
    arr[3] = 77
    updateNode(seg_array,st_index,start,end,3,77)
    print(seg_array)

    #
