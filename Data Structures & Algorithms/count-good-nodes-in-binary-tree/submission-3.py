# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        root_val = root.val
        def dfs(max_seen: int, node: Optional[TreeNode]) -> int:
            if node:
                curr = 0
                if root_val <= node.val and max_seen <= node.val:
                    curr += 1
                new_max_seen = max(max_seen, node.val)
                return curr + dfs(new_max_seen, node.left) + dfs(new_max_seen, node.right)
            return 0
        return dfs(root.val, root)