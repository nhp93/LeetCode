class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<String> list = new ArrayList<>();
        for(int i = 0; i < strs.length; i++) {
            char[] s = strs[i].toCharArray();
            Arrays.sort(s);
            list.add(new String(s));
        }
        HashMap<String, List<String>> groupAna = new HashMap<>();
        for(int j = 0; j< strs.length; j++) {
            if(groupAna.containsKey(list.get(j))) {
                groupAna.get(list.get(j)).add(strs[j]);
            }
            else {
                List<String> temp = new ArrayList<>();
                temp.add(strs[j]);
                groupAna.put(list.get(j), temp);
            }
        }
        return new ArrayList<>(groupAna.values());
    }
}