import java.util.Arrays;

class InsertionSort {
    public static void main(String[] args) {
        int[] arr = { 12, 11, 13, 5, 6 };
        insertion_sort(arr);
        System.out.println("Sorted array: " + Arrays.toString(arr));
    }

    public static void insertion_sort(int[] arr) {
        int size = arr.length;

        for (int i = 1; i < size; i++) {
            int current = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > current) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }

            arr[j + 1] = current;
        }
    }
}