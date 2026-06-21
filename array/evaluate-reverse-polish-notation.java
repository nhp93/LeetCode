class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> stack = new Stack<>();
        int len = tokens.length;
        for (int i = 0; i < len; i++) {
            if (tokens[i].equals("+") || tokens[i].equals("-") || tokens[i].equals("*") || tokens[i].equals("/")) {
                if (stack.size() < 2) {
                    return 0;
                }
                else {
                    int val1 = Integer.parseInt(stack.pop());
                    int val2 = Integer.parseInt(stack.pop());
                    if (tokens[i].equals("+")) {
                        int plus = val1 + val2;
                        stack.push(String.valueOf(plus));
                    }
                    else if (tokens[i].equals("-")) {
                        int minus = val2 - val1;
                        stack.push(String.valueOf(minus));
                    }
                    else if (tokens[i].equals("*")) {
                        int times = val1 * val2;
                        stack.push(String.valueOf(times));
                    }
                    else if (tokens[i].equals("/")) {
                        int divide = val2 / val1;
                        stack.push(String.valueOf(divide));
                    }
                }
            }
            else {
                stack.push(tokens[i]);
            }
        }
        return Integer.parseInt(stack.pop());
    }
}