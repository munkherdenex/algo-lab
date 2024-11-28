def binary_search_recursive(arr, left, right, target):

    if left > right:
        return -1  

    mid = (left + right) // 2  

    if arr[mid] == target:
        return mid  
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, right, target)
    else:
        return binary_search_recursive(arr, left, mid - 1, target)

sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
target_value = 7

result = binary_search_recursive(sorted_array, 0, len(sorted_array) - 1, target_value)

print("Index:", result) 
