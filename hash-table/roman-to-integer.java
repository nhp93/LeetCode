class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> values = new HashMap<>();
        values.put('M', 1000);
        values.put('D', 500);
        values.put('C', 100);
        values.put('L', 50);
        values.put('X', 10);
        values.put('V', 5);
        values.put('I', 1);

        int sum = 0;

        for (int i = 0; i < s.length(); i ++) {
            int curr = values.get(s.charAt(i));

            if (i < s.length() - 1) {
                int next = values.get(s.charAt(i+1));

                if (curr < next) {
                    sum -= curr;
                }
                else {
                    sum += curr;
                }
            }
            else {
                sum += curr;
            }

        }
        return sum;
    }
}