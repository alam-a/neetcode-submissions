class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lc = set(nums)
        m = 0            

        for num in nums:
            if num not in lc:
                continue
            c = 1
            t = num
            while t-1 in lc:
                c+=1
                t-=1
            t = num
            while t+1 in lc:
                c+=1
                t+=1
            m = max(c, m)
        return m