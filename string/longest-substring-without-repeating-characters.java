class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int maxLength = 0;
        int left = 0;
        for(int i = 0; i < s.length(); i++) {
            while(set.contains(s.charAt(i))) {
                set.remove(s.charAt(left));
                left++;
            }
            set.add(s.charAt(i));
            maxLength = Math.max(maxLength, set.size());
        }
        return maxLength;
    }
}