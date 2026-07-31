class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        i, L = 0, len(path)
        while i < len(path):
            # print(i, path[i], stack)
            if path[i] == '/':
                while i < L and path[i] == '/':
                    i += 1
            elif path[i] == '.':
                start = i
                while i < L and path[i] != '/':
                    i += 1
                if i - start == 2 and stack:
                    stack.pop()
                elif i - start > 2:
                    stack.append(path[start:i])
            else:
                start = i
                while i < L and path[i] != '/':
                    i += 1
                stack.append(path[start:i])
        from functools import reduce
        print(stack)
        res = reduce(lambda x, y: x + '/' + y, list(stack), '')
        return res if res else '/'
