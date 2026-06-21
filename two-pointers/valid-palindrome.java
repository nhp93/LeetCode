class Solution {
    public boolean isPalindrome(String s) {
        String clean = s.replaceAll("[\\p{Punct}]", "");
        clean = clean.replaceAll(" ","");
        clean = clean.toLowerCase();
        int right = clean.length() - 1;
        int left = 0;
        while(left < right) {
            if(clean.charAt(left) == clean.charAt(right)) {
                left++;
                right--;
            }
            else {
                return false;
            }
        }
        return true;
    }
}