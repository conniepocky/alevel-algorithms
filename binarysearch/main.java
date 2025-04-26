public class main {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        System.out.println(binary_search(arr, 3, 0, arr.length - 1)); 
    }

    public static int binary_search(int[] arr, int target, int left, int right) {
        if (arr == null || arr.length == 0) {
            return -1; 
        }

        int mid = (left + right) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            return binary_search(arr, target, mid + 1, right);
        } else {
            return binary_search(arr, target, left, mid - 1);
        }
    }
}
