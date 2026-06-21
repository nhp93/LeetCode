class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<List<Integer>> lol = new ArrayList<>();
        for(int i = 0; i <= rowIndex; i++) {
            List<Integer> curr = new ArrayList<>();
            if (i == 0) {
                curr.add(1);
            }
            
            else if(i == 1) {
                curr.add(1);
                curr.add(1);
            }
            else {
                List<Integer> prev = lol.get(i-1);
                curr.add(1);
                for(int j = 1; j < i; j++) {
                    curr.add(j, prev.get(j-1)+prev.get(j));
                }
                curr.add(1);
            }
            lol.add(curr);
        }
        return lol.get(rowIndex);
    }
}