from typing import List, Tuple
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sparse_ranked_list = [[] for _ in nums]
        for num, count in freq.items():
            sparse_ranked_list[count-1].append(num)

        res = []
        for elems in sparse_ranked_list[::-1]:
            if len(res) > k:
                break
            res.extend(elems)
        return res[:k]



