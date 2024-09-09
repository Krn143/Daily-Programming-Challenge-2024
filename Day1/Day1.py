def sort012(arr):
    # Initialize pointers for the low, mid, and high positions
    low, mid, high = 0, 0, len(arr) - 1

    # Traverse the array until mid pointer passes the high pointer
    while mid <= high:
        if arr[mid] == 0:
            # If the element is 0, swap it with the element at 'low' pointer
            # Increment both 'low' and 'mid' pointers
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # If the element is 1, just move the 'mid' pointer ahead
            mid += 1
        else:  # arr[mid] == 2
            # If the element is 2, swap it with the element at 'high' pointer
            # Decrement the 'high' pointer
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Example usage
arr = [0, 1, 2, 1, 0, 2, 1, 0]
print("Sorted array:", sort012(arr))
