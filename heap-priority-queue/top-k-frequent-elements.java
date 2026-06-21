class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            if(map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i]) + 1);
            }
            else{
                map.put(nums[i], 1);
            }
        }
        int index = 0;
        int res[] = new int[k];
        while(k > 0) {
            int maxKey = 0;
            int maxFreq = 0;
            for(Integer key: map.keySet()) {
                if(map.get(key) > maxFreq) {
                    maxFreq = map.get(key);
                    maxKey = key;
                }
            }
            res[index++] = maxKey;
            map.remove(maxKey);
            k--;
        }
        return res;
    }
}