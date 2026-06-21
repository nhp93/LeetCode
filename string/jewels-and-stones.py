class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_dict = Counter(jewels)
        s_dict = Counter(stones)
        count = 0
        for keyJ in j_dict:
            if keyJ in s_dict:
                count += s_dict[keyJ]
        return count