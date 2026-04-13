class Solution:

    def encode(self, strs: List[str]) -> str:
        return "" if not strs else "".join(map(lambda s: f"{len(s)}_{s}", strs))
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            n = 0
            while s[i] != '_':
                n = (n * 10) + int(s[i])
                i += 1
            i += 1
            res.append(s[i:i+n])
            i=i+n
        return res