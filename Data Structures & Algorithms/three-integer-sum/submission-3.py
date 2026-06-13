class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        L = len(nums)
        nums.sort()
        res = []
        for i in range(L-2):
            target = -(nums[i])
            l, r = i+1, L-1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    break
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return res
