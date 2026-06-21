class Solution {
    public int bitwiseComplement(int n) {
        int r = 0;
        StringBuilder ans = new StringBuilder(); 
        StringBuilder newAns = new StringBuilder();
        int result = 0;
        if(n == 0) {
            return 1;
        }
        while(n > 0) {
            if(n%2 == 1) {
                ans.append('1');
            }
            else {
                ans.append('0');
            }
            n /= 2;
        }
        for(int i = 0; i < ans.length(); i++) {
            if(ans.charAt(i) == '1') {
                newAns.append('0');
            }
            else {
                newAns.append('1');
            }
        }
        for(int j = newAns.length() - 1; j >= 0; j--) {
            if(newAns.charAt(j) == '1') {
                result += (int)Math.pow(2, j);
            }
        }
        return result;
    }
}