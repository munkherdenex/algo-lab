def connectingTowns(n, routes):
    MOD = 1234567
    total_routes = 1
    for route in routes:
        total_routes = (total_routes * route) % MOD
    return total_routes

if __name__ == "__main__":
    T = int(input().strip())  
    results = []
    for _ in range(T):
        n = int(input().strip())  
        routes = list(map(int, input().strip().split()))  
        results.append(connectingTowns(n, routes))
    for res in results:
        print(res)
