class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        L = len(nums)
        for i in range(L):
            target = 0 - nums[i]
            l, r = i+1, L-1
            while l < r:
                if nums[l] + nums[r] == target:
                    sol.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return [list(i) for i in set(sol)]


        












