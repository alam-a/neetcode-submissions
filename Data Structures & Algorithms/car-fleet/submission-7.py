class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_by_pos = sorted(zip(map(lambda pos: target - pos, position), speed))
        times = [d_s[0]/d_s[1] for d_s in sorted_by_pos]
        fleet_count = 1
        last_time = times[0]
        for time in times[1:]:
            if time > last_time:
                last_time = time
                fleet_count += 1
        return fleet_count