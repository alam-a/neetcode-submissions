class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        o, t, oc, tc = None, None, 0, 0
        for num in nums:
            if o == num or (oc == 0 and t != num):
                oc += 1
                o = num
            elif t == num or tc == 0:
                tc += 1
                t = num
            else:
                oc -= 1
                tc -= 1
        print(o, oc, t, tc)
        oc, tc = 0, 0
        for num in nums:
            if o == num:
                oc += 1
            elif t == num:
                tc += 1
        print(o, oc, t, tc)
        res = []
        if oc > len(nums)//3:
            res.append(o)
        if tc > len(nums)//3:
            res.append(t)
        return res