# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Do dfs searching height in each subtree 
        And then compare globally
        """
        self.res = True
        def dfs(node):

            if not node:
                return 0

            left = node.left
            right = node.right

            lh = dfs(left)
            rh = dfs(right)
            if abs(lh - rh) > 1:
                self.res = False

            return 1 + max(lh, rh)

        dfs(root)
        return self.res