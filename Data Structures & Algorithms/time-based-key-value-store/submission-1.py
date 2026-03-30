class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            row = self.store[key]
            print(row)
            if timestamp > row[-1][0]:
                return row[-1][1]
            elif timestamp >= row[0][0]:
                l, r = 0, len(row)-1
                res = ""
                while l <= r:
                    mid = (l + r) // 2
                    if row[mid][0] <= timestamp:
                        l = mid + 1
                        res = row[mid][1]
                    else:
                        r = mid - 1
                return res
        return ""