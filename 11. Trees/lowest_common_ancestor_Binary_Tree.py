class Recursive_Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        if current.val == p.val or current.val == q.val:
            return current
        if not current:
            return None
        left = right = None
        if current.left:
            left = self.lowestCommonAncestor(current.left,p,q)
        if current.right:
            right = self.lowestCommonAncestor(current.right,p,q)
        if left and right:
            return current
        return right if left is None else left

        