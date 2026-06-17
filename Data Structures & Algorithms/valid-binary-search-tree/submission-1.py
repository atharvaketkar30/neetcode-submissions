# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Using DFS check for each node if its between left and right
        If any node violates, then return False
        """

        def dfs(node, l_min, r_max):
            if not node:
                return True
            if not (l_min < node.val < r_max):
                return False
            
            return dfs(node.left, l_min, node.val) and dfs(node.right, node.val, r_max)
        
        return dfs(root, -1001, 1001)
        