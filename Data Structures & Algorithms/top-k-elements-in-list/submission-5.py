class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        sparse_lists = [[] for _ in range(len(nums) + 1)]
        for k, v in freq.items():
            sparse_lists[v].append(k)
        res = []
        for sparse_list in sparse_lists[::-1]:
            res.extend(sparse_list)
            if len(res) >= k:
                break

        return res[:k-1]