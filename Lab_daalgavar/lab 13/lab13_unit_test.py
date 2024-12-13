import unittest

def connectingTowns(n, routes):
    MOD = 1234567
    total_routes = 1
    for route in routes:
        total_routes = (total_routes * route) % MOD
    return total_routes

class TestConnectingTowns(unittest.TestCase):

    def test_single_case(self):
        self.assertEqual(connectingTowns(3, [1, 3]), 3)
        
    def test_all_same_routes(self):
        self.assertEqual(connectingTowns(4, [2, 2, 2]), 8)

    def test_large_case(self):
        self.assertEqual(connectingTowns(5, [1000, 1000, 1000, 1000]), 993007)

    def test_single_route(self):
        self.assertEqual(connectingTowns(2, [123]), 123)

    def test_large_routes(self):
        self.assertEqual(connectingTowns(3, [1000, 1000]), 49)

if __name__ == "__main__":
    unittest.main()