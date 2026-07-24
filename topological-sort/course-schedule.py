from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for p in prerequisites:
            u, v = p[0], p[1]
            graph[u].append(v)
        visited = set()
        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            for value in graph[course]:
                if not dfs(value):
                    return False
            visiting.remove(course)        
            visited.add(course)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True