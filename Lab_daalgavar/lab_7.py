class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(capacity, weights, values):
    n = len(weights)
    items = [Item(values[i], weights[i]) for i in range(n)]
    
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    max_value = 0 
    for item in items:
        if capacity >= item.weight:
            max_value += item.value
            capacity -= item.weight
        else:
            max_value += item.ratio * capacity
            break
    
    return max_value

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Maximum value:", fractional_knapsack(capacity, weights, values))
