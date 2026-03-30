class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import deque
        stack = deque()
        stack.append((temperatures[-1], len(temperatures)-1))
        dbw = [0 for _ in range(len(temperatures))] #days_before_warmer

        # starting from second last and moving towards first index
        # if a temperature is found which is higher than the top in the stack
        # we pop the item from stack, and if there is still a element in stack
        # then we take top_of_stack - index_of_popped and update in the days_before_warmer array
        for i in range(len(temperatures) - 2, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]: 
                top, ti = stack.pop()
                if stack and top != stack[-1][0]:
                    dbw[ti] = stack[-1][1] - ti
            stack.append((temperatures[i], i))
        
        # for the items still in the stack, we pop them one by one and update
        # dbw array for them, the last item is the highest temperature in the list
        # for which we don't need to update the array as there is no next higher temperature
        while stack:
            temp, i = stack.pop()
            if stack:
                dbw[i] = stack[-1][1] - i
        return dbw