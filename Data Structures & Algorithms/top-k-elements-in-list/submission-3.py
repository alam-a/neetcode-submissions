class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqd = {}
        for num in nums:
            freqd[num] = freqd.get(num, 0) + 1
        
        freq = [[] for _ in range(len(nums))]
        for num, count in freqd.items():
            freq[count-1].append(num)
        res = []
        for nl in freq[::-1]:
            if nl:
                res.extend(nl)
            if len(res) > k:
                break
        return res[:k]