from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) >= n or len(trust) < n - 2:
            return -1

        graph = defaultdict(int)
        # visited = set()
        # visiting = set()
        # def dfs(person):
        #     if person in visiting:
        #         return False
        #     if person in visited:
        #         return True
        #     for c in graph[person]:
        #         if dfs(c):
        #             return True
        #     visiting.remove(course)        
        #     visited.add(course)
        #     return False
        trusted = trust[0][1]

        for p, t in trust:
            if t != trusted or p == trusted:
                return -1
        return trusted


        