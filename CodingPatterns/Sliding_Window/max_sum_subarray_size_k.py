# Given an array of positive numbers and a positive number k
# find the maximum sum of any contiguous subarray of size k

# Time: O(N)
# Space: O(1)

def max_sub_array_of_size_k(k, arr):

    win_sum = 0
    max_sum = 0
    startWin = 0

    # window right bound is at end of array
    for endWin in range(len(arr)):
        win_sum += arr[endWin]  # add incoming element (right side)
        win_size = endWin - startWin + 1  # current window size

        if (win_size == k):  # if window size is valid
            max_sum = max(win_sum, max_sum)  # store the larger sum
            win_sum -= arr[startWin]  # subtract outgoing element (left side)
            startWin += 1  # increment window left bound

    return max_sum


def main():
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(1, [2, 3, 4, 1, 5])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(4, [1, 2, 3, 4])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(3, [1, 2, 3, 4])))


main()
