class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stack = []
        for s in range(len(sandwiches)-1, -1, -1):
            stack.append(sandwiches[s])
        
        dq = deque()

        for i in range(len(students)):
            dq.append(students[i])
        count = 0
        while dq:
            if dq[0] == stack[-1]:
                stack.pop()
                dq.popleft()
                count = 0
            else:
                dq.append(dq.popleft())
                count += 1
            
            if count == len(dq):
                break
        return len(stack)
        

