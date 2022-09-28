class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #iterative
        Q = deque()
        Q.append(root)
        Q.append(root)
        while Q:
            n1 = Q.pop()
            n2 = Q.pop()
            if (n1 is None and n2 is None):
                continue
            if (n1 is None or n2 is None):
                return False
            if n1.val != n2.val: 
                return False
            Q.append(n1.left)
            Q.append(n2.right)
            Q.append(n1.right)
            Q.append(n2.left)
        return True
            

#recursive
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def ismirror(n1,n2):
            if n1 is None and n2 is None: 
                return True
            if n1 is None or n2 is None:
                return False       
            return (n1.val == n2.val) and ismirror(n1.left,n2.right) and ismirror(n1.right,n2.left)
        return ismirror(root,root)