class Solution {
    public String simplifyPath(String path) {
        int i = 0;
        StringBuilder sb = new StringBuilder(path);
        while (i < sb.length() - 1) {
            if (sb.charAt(i) == '/' && sb.charAt(i + 1) == '/') {
                sb.deleteCharAt(i);
            }
            else {
                i++;
            }
        }
        if (sb.charAt(0) == '/') {
            sb.deleteCharAt(0);
        }
        Stack<String> stack = new Stack<>();
        String cleanedPath = sb.toString();
        String[] cleaned = cleanedPath.split("/");

        
        for (String s: cleaned) {
            if (s.equals("..")) {
                if (!stack.isEmpty()) {
                    stack.pop();
                }
            }
            else if (!s.equals(".") && !s.equals("")) {
                stack.push(s);
            }
        }
        
        if (stack.isEmpty()) {
            return "/";
        }
        StringBuilder result = new StringBuilder();
        for (String w : stack) {
            result.append("/").append(w);
        }
        
        return result.toString();
    }
}