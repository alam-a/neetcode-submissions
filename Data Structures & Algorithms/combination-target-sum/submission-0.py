class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        from collections import defaultdict
        res = set()
        path = defaultdict(int)
        def find(curr):
            if curr == target:
                this = []
                for k, v in path.items():
                    for i in range(v):
                        this.append(k)
                res.add(tuple(this))
                return

            for num in nums:
                if curr + num <= target:
                    path[num] += 1
                    find(curr+num)
                    path[num] -= 1
        find(0)
        return [list(t) for t in res]