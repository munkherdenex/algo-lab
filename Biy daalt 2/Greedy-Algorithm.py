def fractional_knapsack(weights, values, capacity):
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]
    items.sort(reverse=True)
    
    total_value = 0
    for value_per_weight, weight, value in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += value_per_weight * capacity
            break
    return total_value

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Max Value:", fractional_knapsack(weights, values, capacity))
