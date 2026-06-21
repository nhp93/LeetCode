class MinStack {

    ArrayList<Integer> ls;
    public MinStack() {
        ls = new ArrayList<>();
    }
    
    int count = 0;
    int min = Integer.MAX_VALUE;
    Stack<Integer> minStack = new Stack<>();

    public void push(int val) {
        ls.add(val);
        count += 1;
        min = Math.min(min, val);
        if (minStack.isEmpty() || val <= minStack.peek()) {
            minStack.push(val);
        }
    }
    
    public void pop() {
        int removed = ls.remove(count - 1);
        count -= 1;
        if (removed == minStack.peek()) {
            minStack.pop();
        }
    }
    
    public int top() {
        return ls.get(count - 1);
    }
    
    public int getMin() {
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */