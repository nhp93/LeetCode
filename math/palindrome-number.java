class Solution {
    public boolean isPalindrome(int x) {
        String s = Integer.toString(x); 
        if (s.charAt(0) == '-') {
            return false;
        }
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != s.charAt(s.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}