import unittest
def optimal_bst(keys, freq, n):
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = freq[i]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            for r in range(i, j + 1):
                cost = sum(freq[i:j+1]) 
                if r > i:
                    cost += dp[i][r - 1]
                if r < j:
                    cost += dp[r + 1][j]
                
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]

class TestOptimalBST(unittest.TestCase):

    def test_example_case(self):
        keys = [5, 6]
        freq = [17, 25]
        n = len(keys)
        expected_cost = 59
        self.assertEqual(optimal_bst(keys, freq, n), expected_cost)

if __name__ == '__main__':
    unittest.main()
