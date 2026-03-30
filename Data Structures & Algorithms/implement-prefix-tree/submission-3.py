class TrieNode:
    def __init__(self):
        self.nodes: Dict[str, TrieNode] = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()        

    def insert(self, word: str) -> None:
        head = self.trie
        for char in word:
            if char not in head.nodes:
                head.nodes[char] = TrieNode()
            head = head.nodes[char]
        head.is_word = True

    def search(self, word: str) -> bool:
        head = self.trie
        for char in word:
            if char not in head.nodes:
                return False
            head = head.nodes[char]
        return head.is_word 

    def startsWith(self, prefix: str) -> bool:
        head = self.trie
        for char in prefix:
            if char not in head.nodes:
                return False
            head = head.nodes[char]
        return True
        