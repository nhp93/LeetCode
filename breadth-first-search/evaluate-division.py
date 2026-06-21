class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        
        map = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            map[u][v] = val
            map[v][u] = 1.0 / val

        for j in range(len(queries)):
            start = queries[j][0]
            end = queries[j][1]
            visited = set({start})
            queue = deque([(start, 1.0)])
            true_val = -1.0
            if start not in map or end not in map:
                res.append(-1.0)
                continue    
            if start == end:
                res.append(1.0)
                continue


            while queue:
                curr, weight = queue.popleft()
                for neighbor, val in map[curr].items():
                    if neighbor == end:
                        true_val = weight * val
                        continue
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, weight * val))
                print ((queue, true_val))
                    
            res.append(true_val)
        return res