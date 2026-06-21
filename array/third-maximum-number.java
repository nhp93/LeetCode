class Solution {
    public int thirdMax(int[] nums) {
        int max = Integer.MIN_VALUE;
        int sec = Integer.MIN_VALUE;
        int target = Integer.MIN_VALUE;
        List<Integer> dif = new ArrayList<>();
        for (int i: nums) {
            if (i > max) {
                max = i;
            }
        }      
        for (int i: nums) {
            if (!dif.contains(i)) {
                dif.add(i);
            }
        }
        if (dif.size() < 3) {
            return max;
        }
        for (int i: nums) {
            if (i > sec && i < max) {
                sec = i;
            }
        }
        for (int i: nums) {
            if (i > target && i < sec) {
                target = i;
            }
        }
        return target;
    }
}