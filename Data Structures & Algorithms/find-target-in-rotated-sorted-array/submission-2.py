class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        mi = 0 #min_index
        while l <= r:
            if nums[l] < nums[r] and nums[mi] < nums[l]:
                mi = l
                break
            mid = (l+r)//2
            if nums[l] > nums[mid]:
                if nums[mi] > nums[mid]:
                    mi = mid
                r = mid-1
            else:
                l = mid+1
        print(nums[mi])
        def binary_search(l, r):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        ls = binary_search(0, mi-1)
        if ls != -1:
            return ls
        rs = binary_search(mi, len(nums)-1)
        if rs != -1:
            return rs
        return -1

