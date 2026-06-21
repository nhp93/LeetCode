class Solution {
    public String decodeString(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != ']') {
                stack.push(s.charAt(i));
            }
            else {
                StringBuilder part = new StringBuilder();
                String mult = "";
                while (!stack.isEmpty() && !Character.isDigit(stack.peek()) && stack.peek() != '[') {
                    part.append(stack.pop());
                }
                stack.pop();
                while (!stack.isEmpty() && Character.isDigit(stack.peek())) {
                    mult = stack.pop() + mult;
                }
                String res = "";
                for (int r = 0; r < Integer.valueOf(mult); r++) {
                    res += part;
                }
                for (int j = res.length() - 1; j >= 0; j--) {
                    stack.push(res.charAt(j));
                }
            }
        }
        String final1 = "";
        while (!stack.isEmpty()) {
            final1 = stack.pop() + final1;
        }
        return final1;
    }
}