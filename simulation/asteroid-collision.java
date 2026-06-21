class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < asteroids.length; i++) {
            if (asteroids[i] > 0) {
                stack.push(asteroids[i]);
            }
            else {
                int realSize = Math.abs(asteroids[i]);

                while (!stack.isEmpty() && stack.peek() < realSize && stack.peek() > 0) {
                    stack.pop();
                }

                if(!stack.isEmpty() && realSize == stack.peek()) {
                    stack.pop();
                }

                else if (stack.isEmpty() || stack.peek() < 0) {
                    stack.push(asteroids[i]);
                }
            }
        }
        int[] res = new int[stack.size()];
        for (int i = res.length - 1; i >= 0; i--) {
            res[i] = stack.pop();
        }
        return res;
    }
}