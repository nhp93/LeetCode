class Solution {
    public String findDifferentBinaryString(String[] nums) {
        int len = nums.length;
        int sum = 1;
        int lenEach = nums[0].length();
        StringBuilder model = new StringBuilder();
        StringBuilder ans = new StringBuilder();
        for(int m = 0; m < lenEach; m++) {
            sum *= 2;
        }
        if(len == sum) {
            return null;
        }
        for(int a = 0; a < lenEach; a++) {
            model.append('0');
        }
        for (int i = lenEach - 1; i >= 0; i--) {
            for (int j = 0; j < len; j++) {
                if (nums[j].equals(model.toString())) {
                    model.setCharAt(i, '1');
                }
            }
        }
        return model.toString();
    }
}