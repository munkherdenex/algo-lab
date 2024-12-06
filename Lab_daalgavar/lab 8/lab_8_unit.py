import unittest

class TestCoinChange(unittest.TestCase):

    def test_example_case(self):
        coins = [1, 2, 5]
        amount = 11
        self.assertEqual(coin_change(coins, amount), 3)

    def test_impossible_case(self):
        coins = [2]
        amount = 3
        self.assertEqual(coin_change(coins, amount), -1)

    def test_zero_amount(self):
        coins = [1, 2, 5]
        amount = 0
        self.assertEqual(coin_change(coins, amount), 0)

if __name__ == '__main__':
    unittest.main()
