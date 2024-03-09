class Solution {
    public int arrangeCoins(int n) {
        int sum = n;
        for (int i = 1; i <= n; i++){
            sum = sum - i;
            if (sum < 0){
                return i - 1;
            }
            if (sum == 0){
                return i;
            }
        }
        return -1;
        
    }
}