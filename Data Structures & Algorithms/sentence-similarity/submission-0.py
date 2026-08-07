class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        pairs = defaultdict(set)
        for a, b in similarPairs:
            pairs[a].add(b)
            pairs[b].add(a)
        
        for i in range(len(sentence1)):
            word1, word2 = sentence1[i].lower(), sentence2[i].lower()
            if not (word1 == word2 or (word1 in pairs and word2 in pairs[word1])):
                return False
        return True
            
