class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.children = {}
    def __repr__(self) -> str:
        return f"{self.char}: {{ {self.children} }}"

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.R, self.C = len(board), len(board[0])
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        path = set()

        self.trie = TrieNode()
        def create_trie(i, j, node):
            for move in moves:
                ni, nj = i+move[0], j+move[1]
                if (ni, nj) not in path and 0 <= ni < self.R and 0 <= nj < self.C:
                    if board[ni][nj] not in node.children:
                        node.children[board[ni][nj]] = TrieNode()
                    path.add((ni, nj))
                    create_trie(ni, nj, node.children[board[ni][nj]])
                    path.remove((ni, nj))
        for i in range(self.R):
            for j in range(self.C):
                if board[i][j] not in self.trie.children:
                    path.add((i, j))
                    self.trie.children[board[i][j]] = TrieNode()
                create_trie(i, j, self.trie.children[board[i][j]])
        res = []
        for word in words:
            if self.find_word(self.trie, word):
                res.append(word)
        return res

    def find_word(self, root, word):
        node = root
        for char in word:
            print(node.children)
            if char not in node.children:
                return False
            node = node.children[char]
        return True

