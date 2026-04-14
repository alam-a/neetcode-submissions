class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build_tree(inorder: List[int]) -> Optional[TreeNode]:
            if self.pre_index >= len(preorder) or not inorder:
                return None
            node = TreeNode(preorder[self.pre_index])
            mid = find_num(inorder, preorder[self.pre_index])
            self.pre_index += 1
            if mid is not None:
                node.left = build_tree(inorder[0: mid])
                node.right = build_tree(inorder[mid+1:])
            return node

        def find_num(l: List[int], target: int) -> Optional[int]:
            for i in range(len(l)):
                if l[i] == target:
                    return i
        self.pre_index = 0
        return build_tree(inorder)