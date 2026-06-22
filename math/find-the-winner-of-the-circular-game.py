class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        dq = deque()
        for i in range(1, n+1):
            dq.append(i)
        
        while len(dq) > 1:
            for j in range(k-1):
                front = dq[0]
                dq.popleft()
                dq.append(front)
            dq.popleft()
            print(dq)
        return dq[0]