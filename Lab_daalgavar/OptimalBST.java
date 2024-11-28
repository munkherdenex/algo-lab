public class OptimalBST {

    public static int optimalBST(int[] keys, int[] freq, int n) {
        int[][] dp = new int[n][n];

        for (int i = 0; i < n; i++) {
            dp[i][i] = freq[i];
        }

        for (int length = 2; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                dp[i][j] = Integer.MAX_VALUE;

                for (int r = i; r <= j; r++) {
                    int cost = sum(freq, i, j);
                    if (r > i) {
                        cost += dp[i][r - 1];
                    }
                    if (r < j) {
                        cost += dp[r + 1][j];
                    }

                    dp[i][j] = Math.min(dp[i][j], cost);
                }
            }
        }

        return dp[0][n - 1];
    }

    private static int sum(int[] freq, int i, int j) {
        int total = 0;
        for (int k = i; k <= j; k++) {
            total += freq[k];
        }
        return total;
    }

    public static void main(String[] args) {
        int[] keys = {5, 6};
        int[] freq = {17, 25};
        int n = keys.length;
        
        System.out.println("Minimum cost: " + optimalBST(keys, freq, n));
    }
}
