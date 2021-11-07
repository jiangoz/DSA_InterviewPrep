# Given an array containing 0s, 1s and 2s, sort the array in-place.
# You should treat numbers of the array as objects,
# hence, we can’t count 0s, 1s, and 2s to recreate the array.
# The flag of the Netherlands consists of three colors: red, white and blue;
# and since our input array also consists of three different numbers,
# that is why it is called Dutch National Flag problem.

# Time: O(N)
# Space: O(1)

def dutch_flag_sort(arr: list):
    low = 0
    high = len(arr) - 1
    i = 0  # keeps track of iteration

    while i <= high:
        if arr[i] == 0:
            # swap to be at low index
            arr[i], arr[low] = arr[low], arr[i]
            # increment low (allow for open positions to the right)
            low += 1
            # increment i to check next element
            i += 1
        elif arr[i] == 1:
            # no swapping needed (stay in the middle)
            # increment i to check next element
            i += 1
        elif arr[i] == 2:
            # swap to be at high index
            arr[i], arr[high] = arr[high], arr[i]
            # decrement high (allow for open positions to the left)
            high -= 1
            # after the swap the number at index 'i' could be 0, 1 or 2
            # so don't increment i (still need to check)

    return arr


if __name__ == '__main__':
    arr1 = [1, 0, 2, 1, 0]
    arr2 = [2, 2, 0, 1, 2, 0]
    
    assert dutch_flag_sort(arr1) == [0, 0, 1, 1, 2]
    assert dutch_flag_sort(arr2) == [0, 0, 1, 2, 2, 2]
