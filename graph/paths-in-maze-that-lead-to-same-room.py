class Solution:
    def build_graph(self, corridors):
        graph = defaultdict(set)
        for corridor in corridors:
            u, v = corridor[0], corridor[1]
            graph[u].add(v)
            graph[v].add(u)
        return graph
    
    def count_triangles(self, corridors):
        graph = self.build_graph(corridors)
        total = 0
        for corridor in corridors:
            u, v = corridor[0], corridor[1]
            total += len(graph[u] & graph[v])
        return total // 3

    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        res = self.count_triangles(corridors)
        return res