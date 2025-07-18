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
    # Test case 1
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr1)
    print("Sorted array 1 is:", arr1)

    # Test case 2
    arr2 = [5, 1, 4, 2, 8]
    bubble_sort(arr2)
    print("Sorted array 2 is:", arr2)

    # Test case 3
    arr3 = [3, 0, -1, 10, 7]
    bubble_sort(arr3)
    print("Sorted array 3 is:", arr3)

    # Test case 4 (already sorted)
    arr4 = [1, 2, 3, 4, 5]
    bubble_sort(arr4)
    print("Sorted array 4 is:", arr4)

    # Test case 5 (reverse order)
    arr5 = [9, 7, 5, 3, 1]
    bubble_sort(arr5)
    print("Sorted array 5 is:", arr5)