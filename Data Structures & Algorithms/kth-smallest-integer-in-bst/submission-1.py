# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(root):
            if root:
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)
        dfs(root)
        return res[k-1]

    # def __init__(self):
    #     self.c = 0
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     # res = []
    #     c = 0
    #     def dfs(root):
    #         if root:
    #             res = dfs(root.left)
    #             if res:
    #                 return res
    #             self.c = self.c + 1
    #             if self.c == k:
    #                 return root.val
    #             # res.append(root.val)
    #             res = dfs(root.right)
    #             if res:
    #                 return res
    #     return dfs(root)
    #     # return res[k-1]