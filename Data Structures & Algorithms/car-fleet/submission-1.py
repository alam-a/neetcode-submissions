class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - p)/s for p, s in sorted(zip(position, speed))]
        print(time)
        next_time = time[-1]
        fc = 1
        for t in reversed(time[:-1]):
            print(t, next_time)
            if t > next_time:
                next_time = t
                fc += 1
        return fc