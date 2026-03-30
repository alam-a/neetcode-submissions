# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        im = {inorder[i]:i for i in range(len(inorder))} #inorder_map
        print(im)
        root = TreeNode(preorder[0])
        index = im[preorder[0]]
        self.nn = 1 # next_node

        def build_subtree(node, l, r):
            if l > r or self.nn >= len(inorder):
                return
            print(node.val, l, r)

            new_node = TreeNode(preorder[self.nn])
            self.nn += 1
            ni = im[node.val] #node_index
            nni = im[new_node.val] #new_node_index
            if ni > nni:
                node.left = new_node
            else:
                node.right = new_node
            
            build_subtree(new_node, l, nni-1) #build left subtree
            build_subtree(new_node, nni+1, r) #build right subtree

        build_subtree(root, 0, index-1) #build left subtree 
        build_subtree(root, index+1, len(inorder)-1) #build right subtree
        return root
        
            


