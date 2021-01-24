# Given an array of positive numbers and a positive number ‘S,’ find the length of the
# smallest contiguous subarray whose sum is greater than or equal to ‘S’.
# Return 0 if no such subarray exists.

def smallest_subarray_with_given_sum(s, arr):
    # no such subarray exists
    if sum(arr) < s:
        return 0

    winsum = 0
    smallest_len = len(arr)
    winstart = 0
    # window right bound
    for winend in range(len(arr)):
        winsum += arr[winend]  # add incoming element

        while (winsum >= s):  # shrink window as small as possible
            win_size = winend-winstart + 1
            smallest_len = min(smallest_len, win_size)  # take the smaller
            winsum -= arr[winstart]  # shrink window sum
            winstart += 1  # shrink window (from left side)

    return smallest_len


def main():
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(30, [3, 4, 1, 1, 6])))


main()
