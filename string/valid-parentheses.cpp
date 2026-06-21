class Solution {
public:
    bool isValid(string s) {
        int n = s.length();
        stack<char> stack;
        if (n % 2 == 1) {
            return false;
        }
        for (char c: s) {
            if (c == ']' || c == ')' || c == '}') {
                if (stack.empty()) {
                    return false;
                }
                if (stack.top() == '(') {
                    if (c == ')') {
                        stack.pop();
                    }
                    else {
                        return false;
                    }
                }
                else if (stack.top() == '{') {
                    if (c == '}') {
                        stack.pop();
                    }
                    else {
                        return false;
                    }
                }
                else if (stack.top() == '[') {
                    if (c == ']') {
                        stack.pop();
                    }
                    else {
                    return false;
                    }
                }
            }
            else {
                stack.push(c);
            }
        }
        if (stack.empty()) {
            return true;
        }
        return false;
    }
};