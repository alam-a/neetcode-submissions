class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1]*len(nums), [1]*len(nums)
        product = 1
        for i in range(len(nums)):
            product = product * nums[i]
            left[i] = product

        product = 1
        for i in range(len(nums)-1, -1, -1):
            product = product * nums[i]
            right[i] = product
        
        product = [1]*len(nums)
        product[0] = right[1]
        product[len(nums)-1] = left[len(nums)-2]
        for i in range(1, len(nums)-1):
            product[i] = left[i-1] * right[i+1]
        
        return product