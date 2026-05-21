class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0]*26
        for task in tasks:
            freq[ord(task)-ord('A')] += 1
        mtask = [(0, -freq[char]) for char in range(26)] #priority, char, no_of_char_left
        mtask = [i for i in mtask if i[1]!=0]
        
        import heapq
        heapq.heapify(mtask)
        print(mtask)
        counter = 0
        while len(mtask) > 0:
            curr = mtask[0]
            print(curr, counter)
            counter += 1
            if curr[0]+1 <= counter:
                if curr[1] < -1:
                    heapq.heapreplace(mtask, (counter+n, curr[1]+1))
                else:
                    heapq.heappop(mtask)
        return counter
        
