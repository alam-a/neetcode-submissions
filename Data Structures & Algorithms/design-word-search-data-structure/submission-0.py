class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        trie = self.head
        for char in word:
            if char not in trie.children:
                trie.children[char] = TrieNode()
            trie = trie.children[char]
        trie.is_word = True

    def search(self, word: str) -> bool:
        def search_rec(word, trie):
            for i in range(len(word)):
                if word[i] == ".":
                    found = False
                    for term in trie.children:
                        found = found or search_rec(word[i+1:], trie.children[term])
                    return found
                elif word[i] not in trie.children:
                    return False
                trie = trie.children[word[i]]
            return trie.is_word
        return search_rec(word, self.head)


    # def search(self, word: str) -> bool:
    #     trie = self.head
    #     search_in = {}

    #     for char in word:
    #         if not search_in:
    #             if char == ".":
    #                 search_in = {k: v for k, v in trie.children.items()}
    #             elif char not in trie.children:
    #                 return False
    #         else:
    #             if char == ".":
    #                 for term in search_in.keys():
    #                     search_in.remove(terms)

    #             else:
    #                 #prune uneligible keys
    #                 for term in search_in.keys():
    #                     if char not in term.children:
    #                         search_in.remove(term)
    #                 #no eligible children
    #                 if not search_in:
    #                     return False


    #         if search_in:
    #             if char == ".":
    #                 pass
    #             elif 

    #         if search_in and char == ".":
    #             pass
    #             for t in list(search_in):
    #                 search_in.remove(t)
    #         elif char == ".":
    #             search_in = trie.children
    #         elif not search_in and char not in trie.children:
    #             return False
    #         elif search_in and char not in search_in:
    #             return False
    #         elif search_in and char in search_in:
    #             #remove terms which don't match
    #             for term in search_in:
    #                 if term.collections
    #             pass
    #         trie = trie.children[char]
    #     return True
