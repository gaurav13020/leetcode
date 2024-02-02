class Solution {
        public static int peakIndexInMountainArray(int[] arr) {
        int start = 0;
        int end = arr.length - 1;

        while (start < end) {
            int mid = start + (end - start) / 2;
            if (arr[mid] > arr[mid+1]) {
                // you are in dec part of array

                end = mid;
            } else {
                // you are in asc part of array
                start = mid + 1;
            }
        }

        return start; // or return end as both are =
    }
}