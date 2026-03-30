class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        nvalues = [[] for _ in range(len(nums))]
        for num in freq.keys():
            print(num, freq[num])
            nvalues[freq[num]-1].append(num)
        res = []
        print(nvalues)
        print(freq)
        for values in nvalues[::-1]:
            if k == 0:
                break
            if values:
                for val in values:
                    res.append(val)
                    k -= 1
        return res