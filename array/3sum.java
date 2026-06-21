class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        for(int i = 0; i < nums.length; i++) {
            int target = 0 - nums[i];
            int left = i + 1;
            int right = nums.length - 1;
            while(left < right) {
                if(nums[i] + nums[left] + nums[right] == 0) {
                    result.add(List.of(nums[i], nums[left], nums[right]));
                    left++;
                    right--;
                }
                else if(nums[i] + nums[left] + nums[right] > 0) {
                    right--;
                }
                else {
                    left++;
                }
            }
        }
        Set<List<Integer>> set = new HashSet<>();
        for(int s = 0; s < result.size(); s++) {
            set.add(result.get(s));
        }
        return new ArrayList<>(set);
    }
}