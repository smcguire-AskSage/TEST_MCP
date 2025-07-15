import pytest

# Sample sorting algorithm for testing
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test fixture for sorting algorithms
@pytest.fixture
def sample_data():
    return [64, 34, 25, 12, 22, 11, 90]

def test_bubble_sort(sample_data):
    sorted_data = bubble_sort(sample_data)
    assert sorted_data == sorted(sample_data), "Bubble sort failed"

# Additional tests for other sorting algorithms can be added here
