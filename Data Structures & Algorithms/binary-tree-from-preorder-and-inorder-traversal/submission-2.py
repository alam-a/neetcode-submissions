class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.L = len(preorder)
        def build_tree(beg: int, end: int) -> Optional[TreeNode]:
            if self.pre_index >= self.L or not beg < end:
                return None
            node = TreeNode(preorder[self.pre_index])
            mid = find_num(beg, end, preorder[self.pre_index])
            self.pre_index += 1
            if mid is not None:
                node.left = build_tree(beg, mid)
                node.right = build_tree(mid+1, end)
            return node

        def find_num(beg: int, end: int, target: int) -> Optional[int]:
            for i in range(beg, end):
                if inorder[i] == target:
                    return i
        self.pre_index = 0
        return build_tree(0, self.L)