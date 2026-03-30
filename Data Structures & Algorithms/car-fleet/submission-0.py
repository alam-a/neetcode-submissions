class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # ordered by position, position and speed, and then calculate the time
        # taken for a car from the position to reach the target
        ordered = list(map(lambda x: (target-x[0])/x[1], sorted(zip(position, speed))))
        print(ordered)
        fc = 0 #fleet_count
        top = 0
        for time in ordered[::-1]:
            if time > top:
                fc += 1
                top = time
        return fc