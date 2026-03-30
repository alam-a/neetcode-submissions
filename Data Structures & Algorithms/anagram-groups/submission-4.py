from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = {}
        for word in strs:
            freq = [0]*26
            for char in word:
                freq[ord(char)-ord("a")]+=1
            if word in freqs:
                freqs[word] = [tuple(freq), freqs[word][1]+1]
            else:
                freqs[word] = [tuple(freq), 1]
        fmap = {}
        for word, freq_p_count in freqs.items():
            freq, count = freq_p_count
            if freq in fmap:
                for i in range(count):
                    fmap[freq].append(word)
            else:
                fmap[freq] = [word for i in range(count)]
        return list(fmap.values())