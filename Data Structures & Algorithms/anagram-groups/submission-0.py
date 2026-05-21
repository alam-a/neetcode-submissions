class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = {}
        for word in strs:
            freq = [0]*26
            for char in word:
                freq[ord(char)-ord("a")]+=1
            freqs[word] = tuple(freq)
        
        fmap = {}
        for word, freq in freqs.items():
            if freq in fmap:
                fmap[freq].append(word)
            else:
                fmap[freq] = [word]
        print(list(fmap.values()))
        return list(fmap.values())