# Given an array of sorted numbers, remove all duplicates from it.
# You should not use any extra space;
# after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

def remove_duplicates(arr):
    # index of the next non-duplicate element
    next_non_duplicate = 1
    # keeps track of the number of unique elements
    output_len = 1

    i = 1
    while(i < len(arr)):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
            output_len += 1
        i += 1

    return output_len


if __name__ == '__main__':
    arr1 = [2, 3, 3, 3, 6, 9, 9]
    arr2 = [2, 2, 2, 11]
    assert remove_duplicates(arr1) == 4
    assert remove_duplicates(arr2) == 2
