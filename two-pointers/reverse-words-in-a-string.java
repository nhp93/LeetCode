class Solution {
    public String reverseWords(String s) {
        String[] string = s.trim().split("\\s+");
        int len = string.length;
        StringBuilder sb = new StringBuilder();
        for(int i = len - 1; i > 0; i--) {
            sb.append(string[i]);
            sb.append(" ");
        }
        sb.append(string[0]);
        return sb.toString();
    }
}