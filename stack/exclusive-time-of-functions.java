class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        int[] result = new int[n];

        Stack<Integer> stack = new Stack<>();

        for (int i=0; i<logs.size()-1; i++) {
            String[] left = logs.get(i).split(":");
            String[] right = logs.get(i+1).split(":");
            
            if (right[1].equals("start")) { 
                if (left[1].equals("start")) {
                    int interval = Integer.valueOf(right[2]) - Integer.valueOf(left[2]);
                    result[Integer.valueOf(left[0])] += interval;
                    stack.push(Integer.valueOf(left[0]));
                } else { // left[1] = end
                    int interval = Integer.valueOf(right[2]) - Integer.valueOf(left[2]) - 1;
                    if (!stack.isEmpty()) {
                        result[stack.peek()] += interval;
                    }
                }
            } else { // right[1] = end
                if (left[1].equals("start")) {
                    int interval = Integer.valueOf(right[2]) - Integer.valueOf(left[2]) + 1;
                    result[Integer.valueOf(right[0])] += interval;
                } else { // left[1] = end
                    int interval = Integer.valueOf(right[2]) - Integer.valueOf(left[2]);
                    result[stack.pop()] += interval;
                }
            }
        }

        return result;
    }
}