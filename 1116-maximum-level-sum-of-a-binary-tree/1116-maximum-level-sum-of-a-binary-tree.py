# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = []
        def traverse(node, depth):
            if not node:
                return
            if len(sums) == depth:
                sums.append(0)
            
            sums[depth] += node.val

            traverse(node.left, depth+1)
            traverse(node.right, depth+1)
        traverse(root,0)

        return sums.index(max(sums)) + 1



        