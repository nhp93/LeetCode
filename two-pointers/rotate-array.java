class Solution {
    public void rotate(int[] nums, int k) {
        int len = nums.length;
        k = k % len;
        int[] list = new int[len];
        for(int i = 0; i < len; i++) {
            list[(i+k) % len] = nums[i];
        }
        for(int n = 0; n < len; n++) {
            nums[n] = list[n];
        }
    }
}