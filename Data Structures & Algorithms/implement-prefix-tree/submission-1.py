class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        trie = self.head
        for c in word:
            if c not in trie.children:
                trie.children[c] = TrieNode()
            trie = trie.children[c]
        trie.is_word = True

    def search(self, word: str) -> bool:
        trie = self.head
        for c in word:
            if c not in trie.children:
                return False
            trie = trie.children[c]
        return trie.is_word

    def startsWith(self, prefix: str) -> bool:
        trie = self.head
        for p in prefix:
            if p not in trie.children:
                return False
            trie = trie.children[p]
        return True