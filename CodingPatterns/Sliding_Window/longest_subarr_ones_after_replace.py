# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s,
# find the length of the longest contiguous subarray having all 1s

def length_of_longest_substring(arr, k):

    winStart = 0
    max_len = 0
    count_hashmap = {0: 0, 1: 0}

    for winEnd in range(len(arr)):
        # incoming element added to window
        rightElement = arr[winEnd]
        # update hashmap/dict count for incoming element
        if rightElement not in count_hashmap:
            count_hashmap[rightElement] = 0
        count_hashmap[rightElement] += 1

        winSize = winEnd - winStart + 1
        # check if window is invalid, with regards to k
        if (winSize-(count_hashmap[1]) > k):
            # too many zeros exist; more zeros than the allowed k replacements
            # shrink window
            # update count for outgoing element
            count_hashmap[arr[winStart]] -= 1
            winStart += 1
            winSize = winEnd - winStart + 1

        # window is valid;
        max_len = max(max_len, winSize)

    return max_len


# solution without using hashmap/dict
def length_of_longest_substring2(arr, k):
    window_start, max_length, max_ones_count = 0, 0, 0

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1

        # Current window size is from window_start to window_end, overall we have a maximum of 1s
        # repeating 'max_ones_count' times, this means we can have a window with 'max_ones_count' 1s
        # and the remaining are 0s which should replace with 1s.
        # now, if the remaining 0s are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' 0s
        if (window_end - window_start + 1 - max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == '__main__':
    arr1 = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    arr2 = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    assert length_of_longest_substring(arr1, 2) == 6
    assert length_of_longest_substring(arr2, 3) == 9
    assert length_of_longest_substring2(arr1, 2) == 6
    assert length_of_longest_substring2(arr2, 3) == 9
