class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        freq = defaultdict(int)

        for num in nums:
            freq[num]+=1
        kfreq = [[] for i in range(len(nums))]
        print(kfreq)
        for key, value in freq.items():
            kfreq[value-1].append(key)
        print(kfreq)
        
        res = []
        for i in range(len(nums)-1, -1, -1):
            if len(kfreq[i]) > 0 and len(res) <= k:
                res = res + kfreq[i]
        print(res, k, res[:k])
        return res[:k]
