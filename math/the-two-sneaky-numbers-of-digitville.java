class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        HashSet<Integer> map = new HashSet<>();
        int countIndex = 0;
        List<Integer> ans = new ArrayList<>();
        
        for(int i = 0; i < nums.length; i++) {
            if(!map.add(nums[i])) {
                ans.add(nums[i]);
                countIndex++;
            }
        }
        int[] result = new int[countIndex];
        for(int j = 0; j < countIndex ; j++) {
            result[j] = ans.get(j);
        }
        return result;
    }
}