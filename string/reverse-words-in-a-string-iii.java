class Solution {
    public String reverseWords(String s) {
        int leng = s.length();
        String[] given = s.trim().split("\\s++");
        int len = given.length;
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < len; i++) {
            int curLen = given[i].length();
            for(int j = curLen; j > 0; j--) {
                sb.append(given[i].substring(j-1, j));
            }
            sb.append(" ");
        }
        sb.setLength(leng);
        return sb.toString();
    }
}
