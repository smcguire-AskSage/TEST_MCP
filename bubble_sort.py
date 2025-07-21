# Bubble Sort Implementation in Python

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
if __name__ == "__main__":
    # Test Case 1: Original test case
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array 1:", arr1)
    bubble_sort(arr1)
    print("Sorted array 1:", arr1)
    print()
    
    # Test Case 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5]
    print("Original array 2 (already sorted):", arr2)
    bubble_sort(arr2)
    print("Sorted array 2:", arr2)
    print()
    
    # Test Case 3: Reverse sorted array
    arr3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Original array 3 (reverse sorted):", arr3)
    bubble_sort(arr3)
    print("Sorted array 3:", arr3)