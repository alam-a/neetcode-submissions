# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 1
        def traverse(node):
            if not node:
                return
            left = traverse(node.left)
            if left:
                return left
            # print(node.val, self.counter, k)
            if self.counter == k:
                return node.val
            self.counter += 1
            right  = traverse(node.right)
            if right:
                return right
        return traverse(root)

