class Solution {
    int s = 0;
    public int numberOfSteps(int num) {
        if (num == 0){
            return s;
        }
        if (num % 2 == 0){
            s = s + 1;
            return numberOfSteps(num/2);
        }
        s = s + 1;
        return numberOfSteps(num - 1);
    }
}