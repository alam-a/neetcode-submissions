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
                if top == None:
                    res.append('n')
                    continue
                res.append(str(top.val))
                q.append(top.left)
                q.append(top.right)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        elems = data.split(",")
        if elems == [""]:
            return None
        q = collections.deque()
        root = node = TreeNode(int(elems[0]))
        left = True
        # q.append(node)
        for elem in elems[1:]:
            print(f"current parent: {node.val}")
            print(f"node from list: {elem}")

            temp = None if elem == 'n' else TreeNode(int(elem))
            if temp:
                q.append(temp)
            if left:
                print(f"adding in left: {temp.val}") if temp else print("", end="")
                node.left = temp
                left = False
            else:
                print(f"adding in right: {temp.val}") if temp else print("", end="")
                node.right = temp
                left = True
                node = q.popleft() if q else None
            print()
        return root