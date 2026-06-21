class Solution {
    public int[] plusOne(int[] digits) {
        int len = digits.length;
        if (digits[len - 1] != 9) {
            digits[len - 1] ++;
            return digits;
        }
        for (int i = len - 1; i >= 0; i--) {
            if (digits[i] == 9) {
                digits[i] = 0;
            }
            else {
                digits[i]++;
                return digits;
            }
        }
        int[] newList = new int[len + 1];
        newList[0] = 1;
        return newList;
    }
}