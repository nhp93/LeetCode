class Solution {
    static void merge(int[] a, int left, int right) {
        int[] temp = new int[right - left + 1];
        int mid = left + (right-left)/2;
        int i = left;
        int j = mid + 1;
        int k = 0;
        while (i <= mid && j <= right) {
            if(a[i] <= a[j]) {
                temp[k] = a[i];
                i++;
            }
            else {
                temp[k] = a[j];
                j++;
            }
            k++;
        }
        
        while (i <= mid) {
            temp[k] = a[i];
            i++;
            k++;
        }

        while (j <= right) {
            temp[k] = a[j];
            j++;
            k++;
        }
        for (int t = 0; t < temp.length; t++) {
            a[left + t] = temp[t];
        }
    }
    static void mergeSort(int a[], int left, int right) {
        if(left >= right) {
            return;
        }
        int mid = left + (right - left)/2;
        mergeSort(a, left, mid);
        mergeSort(a, mid+1, right);

        merge(a, left, right);
    }
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        mergeSort(arr, 0, arr.length - 1);
        int minDif = arr[1] - arr[0];
        List<List<Integer>> result = new ArrayList<>();
        
        for (int i = 0; i < arr.length - 1; i++) {
            if(arr[i+1] - arr[i] < minDif) {
                minDif = arr[i+1] - arr[i];
            }
        }
        for (int i = 0; i < arr.length - 1; i++) {
            if(arr[i+1] - arr[i] == minDif) {
                List<Integer> pair = new ArrayList<>();
                pair.add(arr[i]);
                pair.add(arr[i+1]);
                result.add(pair);
            }
        }
        return result;
    }
}