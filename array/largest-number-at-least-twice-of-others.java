class Solution {
    public int dominantIndex(int[] nums) {
        int largest = -1;
        int secLargest = -1;
        int index = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > largest) {
                largest = nums[i];
                index = i;
            } 
        }
        for (int n = 0; n < nums.length; n++) {
            if (largest > nums[n] && nums[n] > secLargest) {
                secLargest = nums[n];
            }
        }
        if (largest >= 2 * secLargest) {
            return index;
        }
        else {
            return -1;
        }
    }
}