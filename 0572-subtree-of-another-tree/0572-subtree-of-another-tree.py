# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(left, right):
            if not left and not right:
                return True
            if (left and not right) or (right and not left):
                return False
            if left.val != right.val:
                return False
            
            return sameTree(left.left, right.left) and sameTree(left.right, right.right)
        
        def subTree(root):
            if not root:
                return False
            if sameTree(root, subRoot):
                return True
            return subTree(root.left) or subTree(root.right)
        
        return subTree(root)
        