class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suff, L = [1], [1], len(nums)
        for i in range(L):
            pre.append(pre[i]*nums[i])
            suff.append(suff[i]*nums[L-i-1])
        suff.reverse()
        print(pre, suff)
        res = [0] * L
        for i in range(L):
            res[i] = pre[i] * suff[i+1]
        return res