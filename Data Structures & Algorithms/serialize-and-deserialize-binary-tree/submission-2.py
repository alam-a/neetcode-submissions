# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            for _ in range(len(q)):
                top = q.popleft()
                if not top:
                    res.append("n")
                    continue
                res.append(str(top.val))
                q.append(top.left)
                q.append(top.right)
        res = ",".join(res)
        print(res)
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        q = collections.deque()
        elems = data.split(",")
        root = temp = TreeNode(int(elems[0]))
        next_is_left = True
        for elem in elems[1:]:
            node = TreeNode(int(elem)) if elem != 'n' else None
            if node:
                q.append(node)
            if next_is_left:
                temp.left = node
            else:
                temp.right = node
                temp = q.popleft() if q else None
            next_is_left = not next_is_left
        return root

