import java.util.HashMap;
import java.util.Map;

public class Fibonacci {
    
    public static int fibonacci(int n, Map<Integer, Integer> memo) {
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }

        if (memo.containsKey(n)) {
            return memo.get(n);
        }

        int result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
        memo.put(n, result);
        return result;
    }

    public static void main(String[] args) {
        Map<Integer, Integer> memo = new HashMap<>();

        System.out.println(fibonacci(10, memo)); 
    }
}
