class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for end, beg in prerequisites:
            adj[beg].append(end)

        res = [[] for _ in range(numCourses)]
        visited = set()
        def dfs(curr_course: int, level: int) -> bool:
            if curr_course in visited:
                return False
            res[level].append(curr_course)
            visited.add(curr_course)
            for next_course in adj[curr_course]:
                if not dfs(next_course, level + 1):
                    return False
            visited.remove(curr_course)
            return True
        for course in range(numCourses):
            if adj[course] and not dfs(course, 0):
                return []
        final_list = []
        for course_list in res:
            final_list.extend(course_list)
        final_list.extend(set(range(numCourses)) - set(final_list))
        return final_list
                