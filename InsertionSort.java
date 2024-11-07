import java.io.*;
import java.util.*;

public class InsertionSort {

    public static void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }

    public static void testInsertionSort() throws IOException {
        File file = new File("test_data.txt");
        if (!file.exists()) {
            System.out.println("Error: test_data.txt file not found.");
            return;
        }

        BufferedReader reader = new BufferedReader(new FileReader(file));
        String line = reader.readLine();
        reader.close();
        
        if (line == null || line.isEmpty()) {
            System.out.println("Error: test_data.txt is empty.");
            return;
        }

        String[] strArr = line.split(",");
        int[] arr = Arrays.stream(strArr).mapToInt(Integer::parseInt).toArray();

        System.out.println("Original: " + Arrays.toString(arr));

        insertionSort(arr);

        System.out.println("Sorted: " + Arrays.toString(arr));

        int[] expectedArr = arr.clone();
        Arrays.sort(expectedArr);

        if (Arrays.equals(arr, expectedArr)) {
            System.out.println("Test tentssen!");
        } else {
            System.out.println("Test fail! Expected " + Arrays.toString(expectedArr) + ", got " + Arrays.toString(arr));
        }
    }

    public static void main(String[] args) {
        try {
            testInsertionSort();
        } catch (IOException e) {
            System.out.println("An error: " + e.getMessage());
        }
    }
}
