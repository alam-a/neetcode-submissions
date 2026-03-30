from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        word_freq = {s:0 for s in strs}
        
        for s in strs:
            if word_freq[s]>0:
                word_freq[s]+=1
                continue
            word_freq[s]+=1

            freqs = [0]*26
            for c in s:
                freqs[ord(c)-ord('a')]+=1
            word_map[s] = tuple(freqs)
        
        res = {}
        for word, freq in word_map.items():
            for _ in range(word_freq[word]):
                if freq in res:
                    res[freq].append(word)
                else:
                    res[freq] = [word]
            
        return list(res.values())