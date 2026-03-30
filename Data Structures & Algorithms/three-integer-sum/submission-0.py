class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            comp = 0 - nums[i]
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[j] + nums[k] == comp:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                elif nums[j] + nums[k] < comp:
                    j+=1
                else:
                    k-=1
        
        return list(set([tuple(i) for i in res]))