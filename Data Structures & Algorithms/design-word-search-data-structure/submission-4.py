class TrieNode:
    def __init__(self, char: str = None):
        self.char = char
        self.nodes = {}
        self.is_word = False
    
    def __repr__(self):
        return f"""{{
            char: {self.char},
            is_word: {self.is_word},
            nodes: 
                {{ {self.nodes} }}
        }}"""

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        trie = self.trie
        for char in word:
            if char not in trie.nodes:
                trie.nodes[char] = TrieNode()
            trie = trie.nodes[char]
        trie.is_word = True

    def search(self, word: str) -> bool:
        def dfs(start: int, trie: TrieNode) -> bool:
            trie_node = trie
            for i in range(start, len(word)):
                char = word[i]
                if char == ".":
                    for node in trie_node.nodes.values():
                        if dfs(i+1, node):
                            return True
                    return False
                if char not in trie_node.nodes:
                    return False
                trie_node = trie_node.nodes[char]
            return trie_node.is_word
        return dfs(0, self.trie)








