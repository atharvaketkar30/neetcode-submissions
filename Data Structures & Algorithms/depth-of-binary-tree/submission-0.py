# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        For each node, we return how much length under it
        Post-order DFS as we are combining left and right node answers
        """

        if not root:
            return 0

        stack = [root]
        while stack:
            node = stack.pop()

            nl = self.maxDepth(node.left)
            nr = self.maxDepth(node.right)

            max_depth = max(nl, nr) + 1
        return max_depth

        