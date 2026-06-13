class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        def can_collide(first, second):
            return first > 0 and second < 0

        for asteroid in asteroids:
            # print(stack, asteroid)
            if not stack:
                stack.append(asteroid)
            elif not can_collide(stack[-1], asteroid):
                stack.append(asteroid)
            else:
                while stack and can_collide(stack[-1], asteroid) and abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                if stack and can_collide(stack[-1], asteroid):
                    if abs(stack[-1]) == abs(asteroid):
                        stack.pop()
                elif not stack or not can_collide(stack[-1], asteroid):
                    stack.append(asteroid)
        return list(stack)

