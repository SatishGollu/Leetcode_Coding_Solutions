# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.new_node = root
        def dfs(node):
            if not node:
                return None
            
            if not node.left and not node.right:
                return node
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)
            
            # shuffle connections
            if left_tail:
                left_tail.right =  node.right
                node.right = node.left
                node.left = None
            return right_tail if right_tail else left_tail
        
        dfs(root)

# recursive - time-O(N),Space-O(N)
# iterative - O(N),space-O(1)

class iterative_Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # iterative
        if not root:
            return None
        node = root
        while node:
            #if node has left child
            if node.left:
                #find the right most child
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                #rewire connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            node = node.right
        