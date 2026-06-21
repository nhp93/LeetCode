class Solution {
    public int lengthOfLastWord(String s) {
        String[] a = s.split(" ");
        int len = a.length;
        int ans = a[len-1].length();
        return ans;
    }
}