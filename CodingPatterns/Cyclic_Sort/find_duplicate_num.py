# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
# The array has only one duplicate but it can be repeated multiple times.
# Find that duplicate number without using any extra space.
# You are, however, allowed to modify the input array.

# Time: O(N)
# Space: O(1)

def find_duplicate(nums):
    # TODO: Write your code here

    # sort the numbers
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1
        if i != correct_idx:
            if nums[i] != nums[correct_idx]:
                # not at correct location; do swap
                # (also they are not duplicate numbers (not equal))
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                # found duplicate (equal) numbers
                return nums[i]
        else:
            i += 1

    return -1

# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
# The array has some numbers appearing twice,
# find all these duplicate numbers

# Time: O(N)
# Space: O(N)

def find_all_duplicates(nums):
    duplicateNumbers = []
    # TODO: Write your code here
    # sort the array
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1
        # number is not at correct position
        if i != correct_idx:
            if nums[i] != nums[correct_idx]:
                # number is not duplicate
                # do swap
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                # number is duplicate
                duplicateNumbers.append(nums[i])
                i += 1
        # number is at correct position
        else:
            i += 1

    return duplicateNumbers


if __name__ == '__main__':
    # 4
    print(find_duplicate([1, 4, 4, 3, 2]))
    # 3
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    # 4
    print(find_duplicate([2, 4, 1, 4, 4]))
    # [4, 5]
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    # [3, 5]
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))
