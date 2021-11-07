#  Given an unsorted array of numbers and a target ‘key’,
# remove all instances of ‘key’ in-place and return the new length of the array.

# Time: O(N)
# Space: O(1)

def remove_element(arr, key):
    nextElement = 0  # index of the next element which is not 'key'
    
    for i in range(len(arr)):
        if arr[i] != key:
            # shift the elements to the left
            arr[nextElement] = arr[i]
            nextElement += 1

    return nextElement


if __name__ == '__main__':
    assert remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3) == 4
    assert remove_element([2, 11, 2, 2, 1], 2) == 2
