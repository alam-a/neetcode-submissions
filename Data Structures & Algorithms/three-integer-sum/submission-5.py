class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        L = len(nums)
        nums.sort()
        res = set()
        for i in range(L-2):
            target = -(nums[i])
            l, r = i+1, L-1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.add((nums[i], nums[l], nums[r]))
                    r -= 1
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return list(res)
