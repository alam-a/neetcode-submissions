from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map or timestamp < self.time_map[key][0][0]:
            return ""
        
        timed_values = self.time_map[key]
        l, r = 0, len(timed_values)-1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if timed_values[mid][0] == timestamp:
                return timed_values[mid][1]
            elif timed_values[mid][0] < timestamp:
                res = timed_values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res