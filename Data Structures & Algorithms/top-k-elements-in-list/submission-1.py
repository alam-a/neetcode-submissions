class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nm = {}
        for n in nums:
            if n in nm:
                nm[n] += 1
            else:
                nm[n] = 1
        
        lm = [[] for i in range(len(nums))]
        for n, c in nm.items():
            lm[c-1].append(n)
        
        res = []
        for i in range(len(nums)-1, -1, -1):
            if len(res) > k:
                break
            for n in lm[i]:
                res.append(n)
        return res[:k]