# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #level order traversal
        if not root:
            return ""
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            for i in range(len(q)):
                top = q.popleft()
                if top == 'n':
                    res.append(top)
                    continue
                res.append(str(top.val))
                if top.left:
                    q.append(top.left)
                else:
                    q.append('n')
                if top.right:
                    q.append(top.right)
                else:
                    q.append('n')
        res = ",".join(res)
        print(res)
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        elems = data.split(",")
        print(elems)
        L = len(elems)
        if elems == ['']:
            return None
        root = TreeNode(int(elems[0]))
        q = collections.deque()
        q.append(root)
        c = 1
        while q:
            if c == len(elems):
                break
            for i in range(len(q)):
                top = q.popleft()
                if top == None:
                    c+=1
                    continue
                # print(top.val, c, elems[c])
                if c < L and elems[c] != 'n':
                    top.left = TreeNode(int(elems[c]))
                c+=1
                if c < L and elems[c] != 'n':
                    top.right = TreeNode(int(elems[c]))
                c+=1
                q.append(top.left)
                q.append(top.right)
        return root