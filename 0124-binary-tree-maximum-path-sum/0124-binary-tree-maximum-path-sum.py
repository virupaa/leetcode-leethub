# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            left = max(0, left)
            right = max(0, right)
            
            #With split
            res[0] = max(res[0], left + right + root.val)

            return root.val + max(left, right)
        dfs(root)
        return res[0]



        