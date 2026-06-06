class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #linear search_position
        res = []
        left = None
        merged = False
        for i, interval in enumerate(intervals):
            if merged:
                res.append(interval)
            elif left:
                if newInterval[1] < interval[0]:
                    res.append([left[0], newInterval[1]])
                    res.append(interval)
                    merged = True
                elif newInterval[1] <= interval[1]:
                    res.append([left[0], interval[1]])
                    merged = True
                else:
                    continue
            elif interval[0] <= newInterval[0] <= newInterval[1] <= interval[1]:
                return intervals
            elif newInterval[1] < interval[0]:
                res.append(newInterval)
                res += intervals[i:]
                return res
            elif interval[0] <= newInterval[0] <= interval[1]:
                left = interval
            else:
                res.append(interval)
        if left and not merged:
            res.append([left[0], newInterval[1]])
        elif not merged:
            res.append(newInterval)
        return res

        # def search_position(num: int) -> int:
        #     l, r = 0, len(intervals)-1
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if intervals[mid][0] <= num <= intervals[mid][1]:
        #             return mid
        #         elif n