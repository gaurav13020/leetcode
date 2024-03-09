class Solution {
    public int arrangeCoins(int n) {
        long sum = 0;
        for (long i = 1; i <= n; i++){
            sum = sum + i;
            if (sum > n){
                return (int)i - 1;
            }
            if (sum == n){
                return (int)i;
            }
        }
        return -1;
        
    }
}