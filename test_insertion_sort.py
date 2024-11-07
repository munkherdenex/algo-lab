from insertion_sort import insertion_sort

def test_insertion_sort():
    try:
        with open('test_data.txt', 'r') as file:
            line = file.readline().strip()
        
        if not line:
            print("Error: test_data.txt is empty.")
            return
        
        unsorted_str, expected_str = line.split('|')
        
        unsorted_arr = list(map(int, unsorted_str.strip().split(',')))
        expected_sorted_arr = list(map(int, expected_str.strip().split(',')))
        
        if not unsorted_arr:
            print("Error: The array is empty.")
            return

        print("Original Array:", unsorted_arr)

        sorted_arr = insertion_sort(unsorted_arr)

        print("Sorted Array:", sorted_arr)

        if sorted_arr == expected_sorted_arr:
            print("Test pass!")
        else:
            print(f"Test fail! {expected_sorted_arr}")
    
    except FileNotFoundError:
        print("Error: test_data.txt file not found.")
    except ValueError:
        print("Error: Non-integer value found in the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    test_insertion_sort()
