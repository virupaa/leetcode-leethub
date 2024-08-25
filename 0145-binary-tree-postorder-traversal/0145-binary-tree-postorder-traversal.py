# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        reached = []

        def helper(root):
            if root == None:
                return 

            helper(root.left)
            helper(root.right)
            reached.append(root.val)

        helper(root) 
        return reached
