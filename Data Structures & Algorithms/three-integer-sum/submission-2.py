class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        L = len(nums)
        nums.sort()
        res = set()
        for i in range(L):
            target = 0 - nums[i]
            l, r = i + 1, L-1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l, r = l+1, r-1 
                elif s > target:
                    r -= 1
                else:
                    l += 1
        return list([list(r) for r in res])