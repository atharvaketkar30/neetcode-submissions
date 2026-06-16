# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        for each level, add left and right
        """

        res = []
        tree = deque([root])

        while tree:
            len_q = len(tree)
            level = []

            for i in range(len_q):
                root = tree.popleft()
                if root:
                    tree.append(root.left)
                    tree.append(root.right)

                    level.append(root.val)  

            if level:
                res.append(level)  

        return res       
