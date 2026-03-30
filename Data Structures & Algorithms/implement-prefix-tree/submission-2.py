class Node:
    def __init__(self):
        self.is_word: bool = False
        self.chars = {}

class PrefixTree:
    def __init__(self):
        self.trie = Node()

    def insert(self, word: str) -> None:
        trie = self.trie
        for char in word:
            if char not in trie.chars:
                trie.chars[char] = Node()
            trie = trie.chars[char]
        trie.is_word = True

    def search(self, word: str) -> bool:
        trie = self.trie
        for char in word:
            if char not in trie.chars:
                return False
            trie = trie.chars[char]
        return trie.is_word

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for char in prefix:
            if char not in trie.chars:
                return False
            trie = trie.chars[char]
        return True
        