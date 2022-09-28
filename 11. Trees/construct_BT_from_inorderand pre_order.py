# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#TIME and SPACE - O(N) in the worst case
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_index = 0
        in_order_map = {}
        #hashmap to store values and it's index
        for index,value in enumerate(inorder):
            in_order_map[value] = index
            
        def build(left,right):
            nonlocal pre_index
            if left > right:
                return None
            root_value = preorder[pre_index]
            root = TreeNode(root_value)
            pre_index += 1
            
            root.left = build(left,in_order_map[root_value]-1)
            root.right = build(in_order_map[root_value]+1,right)
            
            return root
        return build(0,len(preorder)-1)
        
            
            
        