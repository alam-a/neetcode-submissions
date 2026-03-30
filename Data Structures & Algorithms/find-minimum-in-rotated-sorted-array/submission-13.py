class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        mini = nums[0]
        while l <= r:
            mid = (l + r) // 2
            print(l, mid, r, mini)
            mini = min(mini, nums[mid])
            if nums[l] < nums[r]:
                mini = min(mini, nums[l])
                break
            elif nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return mini            