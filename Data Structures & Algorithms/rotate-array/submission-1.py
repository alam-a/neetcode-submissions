class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        if k == L:
            return
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1

        reverse(0, L - k - 1)
        reverse(L - k, len(nums)-1)
        reverse(0, len(nums)-1)