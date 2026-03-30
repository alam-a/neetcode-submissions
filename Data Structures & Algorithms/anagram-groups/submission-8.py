class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_freq(string: str) -> tuple[int]:
            freq = [0] * 26
            for char in string:
                freq[ord(char) - ord('a')] += 1
            return tuple(freq)
        from collections import defaultdict
        anagrams = defaultdict(list)

        for string in strs:
            anagrams[get_freq(string)].append(string)
        return list(anagrams.values())