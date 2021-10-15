"""
We are given an array containing n objects. Each object, when created, 
was assigned a unique number from the range 1 to n based on their creation sequence. 
This means that the object with sequence number 3 
was created just before the object with sequence number 4.
Write a function to sort the objects in-place on their creation sequence number 
in O(n)O(n) and without using any extra space. 
For simplicity, let’s assume we are passed an integer array 
containing only the sequence numbers, though each number is actually an object.
"""


def cyclic_sort(nums):
    # TODO: Write your code here
    i = 0

    while i < len(nums):
        correct_idx = nums[i] - 1
        if correct_idx != i:
            # number is not at its correct location
            # swap to its correct location
            # correction index location is: nums[i] - 1
            nums[correct_idx], nums[i] = nums[i], nums[correct_idx]
        else:
            # number is at its correct location
            i += 1

    return nums


if __name__ == '__main__':
    # [1, 2, 3, 4, 5]
    print(cyclic_sort([3, 1, 5, 4, 2]))
    # [1, 2, 3, 4, 5, 6]
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    # [1, 2, 3, 4, 5, 6]
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))
