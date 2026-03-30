# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = 0 #to count the root node as well, we have min of 1 node

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, val):
            if not node:
                return
            if node.val >= val:
                self.res += 1
                val = node.val
            dfs(node.left, val)
            dfs(node.right, val)
        dfs(root, root.val)
        return self.res
