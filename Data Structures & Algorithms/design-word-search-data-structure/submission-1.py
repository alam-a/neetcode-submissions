class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        trie = self.head
        for c in word:
            if c not in trie.children:
                trie.children[c] = TrieNode()
            trie = trie.children[c]
        trie.is_word = True

    def search(self, word: str) -> bool:
        print(f"search: {word}", end = " ---- ")
        def dfs(i: int, trie: TrieNode) -> bool:
            for i in range(i, len(word)):
                print(word[i], end = ", ")
                c = word[i]
                if c == ".":
                    for t, node in trie.children.items():
                        if dfs(i+1, node):
                            return True
                    return False
                elif c not in trie.children:
                    return False
                else:
                    trie = trie.children[c]
            return trie.is_word
        res = dfs(0, self.head)      
        print()
        return res