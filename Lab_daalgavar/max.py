def find_maximum_divide_and_conquer(arr):
    def recursive_max(left, right):
        if left == right:
            return arr[left]
        
        mid = (left + right) // 2
        
        max_left = recursive_max(left, mid)
        max_right = recursive_max(mid + 1, right)
        
        return max(max_left, max_right)
    
    if not arr:
        raise ValueError("Jagsaalt khooson, olokh deed utga baihgui.")
    
    return recursive_max(0, len(arr) - 1)

if __name__ == "__main__":
    example_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    max_value = find_maximum_divide_and_conquer(example_list)
    print(f"Xamgiin ih utga: {max_value}")
