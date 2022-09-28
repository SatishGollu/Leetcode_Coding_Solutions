# using inorder traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        # inorder to get the sorted list of vals
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        nums = inorder(root)

        # for the bst formation 
        def constructBST(nums):
            if len(nums) == 0:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            mid = len(nums) // 2
            root_node = TreeNode(nums[mid])
            root_node.left = constructBST(nums[:mid])
            root_node.right = constructBST(nums[mid+1:])
            return root_node
        
        return constructBST(nums)

# TIME_O(NlogN) space- O(1) if we do not account stack space
# USING ROTATIONS
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode()
        dummy.right = root
        self.recBalance(root, dummy)
        return dummy.right
        
    def rotateLeft(self, root, parent):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        
        if parent.left == root:
            parent.left = new_root
        else:
            parent.right = new_root
        return new_root
    
    def rotateRight(self, root, parent):
        new_root = root.left 
        root.left = new_root.right 
        new_root.right = root
        
        if parent.left == root:
            parent.left = new_root
        else:
            parent.right = new_root
        return new_root
    
    def recBalance(self, node, parent):
        if not node:
            return 0, 0
        
        left_height, left_balance = self.recBalance(node.left, node)
        right_height, right_balance = self.recBalance(node.right, node)
        
        node_balance = left_height - right_height
        
        if node_balance > 1:
            if left_balance < 0:
                self.rotateLeft(node.left, node)
            return self.recBalance(self.rotateRight(node, parent), parent)
        elif node_balance < -1:
            if right_balance > 0:
                self.rotateRight(node.right, node)
            return self.recBalance(self.rotateLeft(node, parent), parent)
        else:
            return max(left_height, right_height) + 1, left_height - right_height