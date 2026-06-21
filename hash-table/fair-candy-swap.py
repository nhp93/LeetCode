class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_set = set(aliceSizes)
        bob_set = set(bobSizes)
        complement = (sum(aliceSizes) - sum(bobSizes)) // 2
        for key in bob_set:
            finding = key + complement
            if finding in alice_set:
                return [finding, key]