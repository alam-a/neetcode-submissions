class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        from collections import deque
        # scheduled_s = set()
        scheduled_q = deque()
        h = []
        # print(Counter(tasks).)
        for task, count in Counter(tasks).items():
            heapq.heappush_max(h, (count, task))
        
        task_count = len(tasks)
        res = 0
        while task_count:
            if h:
                count, task = heapq.heappop_max(h)
                scheduled_q.append((count-1, task))
                task_count -= 1
            else:
                scheduled_q.append((0, ""))

            if len(scheduled_q) > n:
                count, task = scheduled_q.popleft()
                if task and count:
                    heapq.heappush_max(h, (count, task))
            res += 1
        return res

