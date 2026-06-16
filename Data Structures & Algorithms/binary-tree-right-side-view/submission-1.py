# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Input- Binary tree
        Output- Node values visible from right top to bottom
        Repeated op- 
            For each level:
                check if there are both left and right children
                Add rightmost 
        """

        tree = deque([root])
        if not root:
            return []
        ans = [root.val]

        while tree:
            len_level = len(tree)
            lvl_check = False

            for i in range(len_level):
                node = tree.popleft()
                if node.left: 
                    tree.append(node.left)
                    answer = node.left
                    lvl_check = True
                if node.right: 
                    tree.append(node.right)
                    answer = node.right
                    lvl_check = True
                

            if lvl_check: 
                ans.append(answer.val)
        
        return ans
            

        