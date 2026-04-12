class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        starting_courses = set()
        adj = [[] for _ in range(numCourses)]
        for beg, end in prerequisites:
            adj[beg].append(end)
            starting_courses.add(beg)
        path = set()
        def dfs(curr_course: int) -> bool:
            if curr_course in path:
                return False
            path.add(curr_course)
            for next_course in adj[curr_course]:
                if not dfs(next_course):
                    return False
            path.remove(curr_course)
            return True
        for course in starting_courses:
            if not dfs(course):
                return False
        return True