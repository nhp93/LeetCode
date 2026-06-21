class Solution {
    public int hammingWeight(int n) {
        StringBuilder res = new StringBuilder();
        while (n > 0) {
            if (n % 2 == 1) {
                res.append(1);
            }
            n = n / 2;
        }
        return res.length();
    }
}