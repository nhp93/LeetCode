class Solution {
    public int longestConsecutive(int[] nums) {
        int len = nums.length;
        int maxLength = 0;
        int count = 0;
        int maxCount = 0;
        HashSet<Integer> set = new HashSet<>();
        for(int i = 0; i < len; i++) {
            set.add(nums[i]);
        }
        for(int num : set) {
            if(!set.contains(num - 1)) {
                int current = num;
                count = 0;
                while(set.contains(current)) {
                    count++;
                    current++;
                }
                if(count > maxCount) {
                    maxCount = count;
                }
            }
        }
        return maxCount;
    }
}