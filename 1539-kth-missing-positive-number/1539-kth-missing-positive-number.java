class Solution {
    public int findKthPositive(int[] arr, int k) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int i = 1; i <= arr.length + k+1; i++){
            if(!contains(arr, i)){
                list.add(i);
            }
        }
        System.out.println(list);
        return list.get(k-1);
    }
    
    
    
    public boolean contains(int[] arr, int a) {
        for (int i = 0; i < arr.length; i++){
            if(arr[i] == a){
                return true;
            }
        }
        return false;
    }
}