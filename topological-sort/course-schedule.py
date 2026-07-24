from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for p in prerequisites:
            u, v = p[0], p[1]
            graph[u].append(v)
        visited = set()
        for key in graph:
            visited.add(key)
            for value in graph[key]:
                if value in visited:
                    return False
        return True