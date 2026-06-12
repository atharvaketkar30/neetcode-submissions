# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        For each node, we want to calculate height in left and right subtree
        Max diameter thru node is left + right
        Value of node = 1 + max(left, right)
        Need to pass value upwards and also maintain global value
        """

        self.res = 0

        def dfs(node):
            if not node:
                return 0

            left = node.left
            right = node.right

            lh = dfs(left)
            rh = dfs(right)
            self.res = max(self.res, lh + rh)
            print( lh, rh, self.res)
            return 1 + max(lh, rh)

        dfs(root)
        return self.res