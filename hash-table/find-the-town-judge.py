from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        voted = set()
        for u, v in trust:
            voted.add(u)
            graph[v].append(u)
        

        for cand in range(1, n + 1):
            if len(graph[cand]) == n-1 and cand not in voted:
                return cand
        return -1
        