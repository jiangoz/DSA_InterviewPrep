# Given a sorted array,
# create a new array containing squares of all the numbers of the input array in the sorted order.

# Time: O(N)
# Space: O(N)

def make_squares(arr):
    squares = []
    left = 0
    right = len(arr) - 1

    for i in range(len(arr)):
        leftsqr = arr[left] ** 2
        rightsqr = arr[right] ** 2

        # left is smaller or equal
        if (leftsqr <= rightsqr):
            # insert the larger number (rightsqr) to front of list,
            # which will be pushed to back of array eventually (allowing for sorted order)
            squares.insert(0, rightsqr)
            # move right pointer leftwards
            right -= 1
        else:
            # left is greater
            squares.insert(0, leftsqr)
            # move left pointer rightwards
            left += 1

    return squares


if __name__ == '__main__':
    arr1 = [-2, -1, 0, 2, 3]
    arr2 = [-3, -1, 0, 1, 2]
    assert make_squares(arr1) == [0, 1, 4, 4, 9]
    assert make_squares(arr2) == [0, 1, 1, 4, 9]
