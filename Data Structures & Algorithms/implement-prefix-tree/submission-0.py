class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:
    def __init__(self):
        self.head = TrieNode()        

    def insert(self, word: str) -> None:
        trie = self.head
        for char in word:
            if char not in trie.children:
                trie.children[char] = TrieNode()
            trie = trie.children[char]
        trie.is_word = True

    def search(self, word: str) -> bool:
        trie = self.head
        for char in word:
            if char not in trie.children:
                return False
            trie = trie.children[char]
        return trie.is_word

    def startsWith(self, prefix: str) -> bool:
        trie = self.head
        for char in prefix:
            if char not in trie.children:
                return False
            trie = trie.children[char]
        return True
        
        