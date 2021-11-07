# Given an array of sorted numbers and a target sum,
# find a pair in the array whose sum is equal to the given target.

# Time: O(N)
# Space: O(N)

def pair_with_targetsum(arr, target_sum):
    start = 0
    end = len(arr) - 1

    while (start < end):
        curr_sum = arr[start]+arr[end]
        if (curr_sum == target_sum):
            return [start, end]
        elif (curr_sum < target_sum):
            # increase sum by moving start pointer rightward
            start += 1
        else:
            # sum is greater than target sum
            # decrease sum by moving end pointer leftward
            end -= 1

    return 'No such sum exists'

# Alternate solution that uses hashmap/dict
def pair_with_targetsum2(arr, target_sum):
    nums = {}  # to store numbers and their indices
    for i, num in enumerate(arr):
        if target_sum - num in nums:
            return [nums[target_sum - num], i]
        else:
            nums[arr[i]] = i
    return [-1, -1]


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 6]
    arr2 = [2, 5, 9, 11]
    assert pair_with_targetsum(arr1, 6) == [1, 3]
    assert pair_with_targetsum(arr2, 11) == [0, 2]
    assert pair_with_targetsum2(arr1, 6) == [1, 3]
    assert pair_with_targetsum2(arr2, 11) == [0, 2]
