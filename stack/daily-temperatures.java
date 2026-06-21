class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int len = temperatures.length;
        Stack<Integer> waitlist = new Stack<>();
        
        int[] ans = new int[len];
        for (int i = 0; i < len; i++) {
            while (!waitlist.isEmpty() && temperatures[i] > temperatures[waitlist.peek()]) {
                int prev = waitlist.pop();
                ans[prev] = i - prev; 
            }
            waitlist.push(i);
        }
        return ans;
    }
}