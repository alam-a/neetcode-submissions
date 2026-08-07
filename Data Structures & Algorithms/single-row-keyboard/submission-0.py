class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = [0] * 26
        for i in range(26):
            pos[ord(keyboard[i]) - ord('a')] = i
        
        time = pos[ord(word[0]) - ord('a')]
        last = time
        for c in word[1:]:
            curr = pos[ord(c) - ord('a')]
            time += abs(curr - last)
            last = curr
        return time