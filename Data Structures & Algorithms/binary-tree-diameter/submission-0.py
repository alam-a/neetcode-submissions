# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.d = -1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def calculate(root):
            if not root:
                return 0
            ll = calculate(root.left)
            rl = calculate(root.right)
            print(root.val, ll, rl, self.d)
            self.d = max(self.d, ll+rl)
            return max(ll, rl)+1
        calculate(root)
        return self.d