class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rdq = deque()
        ddq = deque()
        for i in range(len(senate)):
            if senate[i] == "R":
                rdq.append(i)
            else:
                ddq.append(i)
        while rdq and ddq:
            if rdq[0] < ddq[0]:
                rdq.append(rdq.popleft() + len(senate))
                ddq.popleft()
            else:
                ddq.append(ddq.popleft() + len(senate))
                rdq.popleft()
        if len(rdq) > 0:
            return "Radiant"
        return "Dire"
