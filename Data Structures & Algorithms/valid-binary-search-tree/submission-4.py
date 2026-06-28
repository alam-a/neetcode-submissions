# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode | None, min_val: float | int, max_val: float | int) -> bool:
            if not node:
                return True
            return (
                min_val < node.val < max_val
                and dfs(node.left, min_val, min(node.val, max_val))
                and dfs(node.right, max(min_val, node.val), max_val)
            )
        return dfs(root, float("-inf"), float("inf"))
