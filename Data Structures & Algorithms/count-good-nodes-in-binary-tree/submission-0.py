# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.c = 0

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, m):
            if not node:
                return
            if node.val >= m:
                self.c += 1
            m = max(m, node.val)
            dfs(node.left, m)
            dfs(node.right, m)
        dfs(root, float("-inf"))
        return self.c