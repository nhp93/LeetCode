class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visited = set() # always use set
        for i in range(len(isConnected)):
            queue = []
            if (i not in visited):
                queue.append(i)
                res += 1
                visited.add(i)
            while len(queue) != 0:
                curr = queue.pop(0)
                visited.add(curr)
                for j in range(len(isConnected)):
                    if (j not in visited) and (isConnected[curr][j] == 1):
                        visited.add(j)
                        queue.append(j)
        return res
        # for key in map
            # for value in map[key]
                # if not visited -> add