# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’.
# Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

# Time: O(N)
# Space: O(1)

def find_missing_number(nums):
    # TODO: Write your code here

    # sort nums then iterate through to check
    i = 0
    while i < len(nums):
        correct_idx = nums[i]
        if i != correct_idx and nums[i] < len(nums):
            # incorrect location; so must swap
            # (also, must have valid index)
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1

    # find the first number missing from its index

    for n in range(len(nums)):
        if nums[n] != n:
            return n
    # all numbers were in correct index/spot,
    # so it must be the largest num missing (n)
    return len(nums)

# We are given an unsorted array containing numbers taken from the range 1 to ‘n’.
# The array can have duplicates, which means some numbers will be missing.
# Find all those missing numbers.

# Time: O(N)
# Space: O(N)

def find_missing_numbers(nums):
    missingNumbers = []
    # TODO: Write your code here
    # sort the numbers
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1
        if i != correct_idx and nums[i] != nums[correct_idx]:
            # number not at correct position AND
            # swapped numbers are not identical (duplicates)
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        correct_idx = nums[i] - 1
        if i != correct_idx:
            missingNumbers.append(i+1)

    return missingNumbers


if __name__ == '__main__':
    # 2
    print(find_missing_number([4, 0, 3, 1]))
    # 7
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
    # missing 4
    print(find_missing_number([0, 2, 3, 1]))

    # [4, 6, 7]
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))

    # [3]
    print(find_missing_numbers([2, 4, 1, 2]))

    # [4]
    print(find_missing_numbers([2, 3, 2, 1]))
