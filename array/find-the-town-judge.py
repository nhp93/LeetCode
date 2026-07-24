from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        voted = set()
        for u, v in trust:
            voted.add(u)
            graph[v].append(u)
        max_len = float('-inf')
        max_cand = 0
        for cand in graph:
            if len(graph[cand]) > max_len and cand not in voted:
                max_len = len(graph[cand])
                max_cand = cand
        if max_cand == 0:
            return -1
        return max_cand
            
        