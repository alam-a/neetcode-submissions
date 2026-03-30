class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        nums.reverse()

        res = []
        curr = []
        self.curr_sum = 0
        def dfs(index):
            if self.curr_sum == target:
                res.append(curr[:])
                return
            elif self.curr_sum > target:
                return

            for i in range(index, len(nums)):
                self.curr_sum += nums[i]
                curr.append(nums[i])
                dfs(i)
                self.curr_sum -= nums[i]
                curr.pop()

        dfs(0)
        return res