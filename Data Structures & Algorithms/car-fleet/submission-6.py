class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_taken = list(map(lambda d_s: d_s[0]/d_s[1], sorted(zip(map(lambda pos: target - pos, position), speed))))
        from collections import deque
        stack = deque()
        stack.append(time_taken[0])
        for time in time_taken:
            if stack[-1] < time:
                stack.append(time)
        return len(stack)