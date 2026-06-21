class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter = Counter(arr)
        keys = sorted(counter.keys())
        count = 0
        for i, key1 in enumerate(keys):
            for j in range(i, len(keys)):
                key2 = keys[j]
                key3 = target - (key1 + key2)
                if key3 in counter and key3 >= key2:
                    if key1 == key2 == key3:
                        count += math.comb(counter[key1], 3)
                    elif key1 == key2:
                        count += math.comb(counter[key1], 2) *  counter[key3]
                    elif key2 == key3:
                        count += math.comb(counter[key2], 2) *  counter[key1]
                    else:
                        count += counter[key1] * counter[key2] * counter[key3]
        return count % (10**9 + 7)