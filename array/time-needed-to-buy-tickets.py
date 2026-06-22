class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        dq = deque()
        for i in range(len(tickets)):
            dq.append(i)
        
        time = 0
        while dq:
            time += 1
            front = dq[0]
            tickets[front] -= 1
            if tickets[front] != 0:
                dq.popleft()
                dq.append(front)
            else:
                dq.popleft()
            if tickets[k] == 0:
                return time
    


