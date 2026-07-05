class Solution:
    from collections import deque
    from collections import defaultdict
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        visited = set()
        count = 0
        for node in range(n):
            if node not in visited:
                count += 1
                dq = deque([node])
                visited.add(node)
                while dq:
                    pop = dq.popleft()
                    for neighbor in graph[pop]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            dq.append(neighbor)
        return count      