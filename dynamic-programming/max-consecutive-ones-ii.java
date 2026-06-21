class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCount = 0;
        int left=0, right=0;
        for (int i=0; i<nums.length; i++) {
            right++;
            if (nums[i] == 0) {
                left = right;
                right = 0;
            }
            maxCount = Math.max(maxCount, left+right);
        }
        return maxCount;
    }
}