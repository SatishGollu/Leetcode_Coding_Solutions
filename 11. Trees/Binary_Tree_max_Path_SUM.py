# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # TIME--O(N), Space--O(H) where H is tree height
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #recursive function #post order
        def max_path(root):
            # This tells that max_path is not a local variable
            nonlocal result 
            #base:
            if not root:
                return 0
            
            left = max_path(root.left)
            right = max_path(root.right)
            #case1 
            max_straight = max(max(left,right)+root.val,root.val)
            max_node = max(max_straight,left+right+root.val)
            result = max(max_node,result)
            
            return max_straight
        
        result = float('-inf')
        max_path(root)
        return result
       
        
        