class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k == len(s):
            return k
        counts = []
        ch, co = s[0], 1 # character and count 
        for c in s[1:]:
            if c == ch:
                co += 1
            else:
                counts.append((ch, co))
                co = 1
                ch = c
        counts.append((ch, co))
        print(counts)

        cc = counts[0][1] # current count
        res = cc # max count
        l, r = 0, 1 # left and right index of the window
        cfr = k # char_flip_remaining
        while l < len(counts):
            print(l, r, end=" ")
            if l + 1 == len(counts):
                res = max(res, counts[l][1])
                break
            if r == len(counts):
                res = max(res, cc)
                l += 1
                cfr, cc = k, counts[l][1]
                r = l+1
                print(cc, cfr, res)
                continue
            print(counts[l], counts[r], cc, cfr, res)
            rch, rco = counts[r][0], counts[r][1]
            if counts[l][0] != rch:
                if cfr > 0:
                    if rco > cfr:
                        cc += cfr
                        res = max(res, cc)
                        cfr, cc = k, rco
                        l = r
                    elif rco == cfr:
                        cc += cfr
                        cfr = 0
                    else:
                        cc += rco
                        cfr -= rco
                else:
                    res = max(res, cc)
                    l = l+1
                    r = l+1
                    cfr, cc = k, counts[l][1]
                    continue
            else:
                cc += rco
            r += 1
            res = max(res, cc)
        return max(res, cc)