class Node:
    def __init__(self):
        self.is_word: bool = False
        self.chars = {}

class WordDictionary:
    def __init__(self):
        self.trie = Node()

    def addWord(self, word: str) -> None:
        trie = self.trie
        for char in word:
            if char not in trie.chars:
                trie.chars[char] = Node()
            trie = trie.chars[char]
        trie.is_word = True

    def search(self, word: str) -> bool:
        def dfs(trie, pattern):
            for i in range(len(pattern)):
                char = pattern[i]
                if char == ".":
                    for t in trie.chars:
                        if dfs(trie.chars[t], pattern[i+1:]):
                            return True
                    return False
                elif char not in trie.chars:
                    return False
                trie = trie.chars[char]
            return trie.is_word
        trie = self.trie
        return dfs(trie, word)