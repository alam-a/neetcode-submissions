class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        p = [1 for i in range(l)]
        s = [1 for i in range(l)]
        p[0], s[-1] = nums[0], nums[-1]
        for i in range(1, l-1):
            p[i] = p[i-1]*nums[i]
            s[l-i-1] = s[l-i]*nums[l-i-1]
        p[-1], s[0] = p[l-2]*nums[-1], s[1]*nums[0] 
        res = [1 for i in range(l)]
        res[0], res[-1] = s[1], p[l-2]
        for i in range(1, l-1):
            res[i] = p[i-1]*s[i+1]
        return res 