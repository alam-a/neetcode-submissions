class Solution:

    def encode(self, strs: List[str]) -> str:
        e = []
        for s in strs:
            e.append(f"{len(s)}_{s}")
        return "".join(e)

    def decode(self, s: str) -> List[str]:
        i = 0
        d = []
        while i < len(s):
            #get length
            length = []
            while s[i].isdigit():
                length.append(s[i])
                i+=1
            length = int("".join(length))
            
            i=i+1 #skip separator
            #get word
            d.append(s[i: i+length])
            i+=length
        return d