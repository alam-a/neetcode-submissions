class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        q = deque()
        q.append(([], nums))
        res = []
        while q:
            for _ in range(len(q)):
                curr, nums = q.popleft()
                res.append(curr)
                for i, num in enumerate(nums):
                    q.append((curr + [num], nums[i+1:]))
        return res