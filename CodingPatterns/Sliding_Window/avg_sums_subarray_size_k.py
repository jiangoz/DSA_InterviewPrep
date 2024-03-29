# Given an array, find the average sums of all contiguous subarrays of size K

# Time: O(N)
# Space: O(N)

def find_averages_of_subarrays(K, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]  # add the next element
        win_size = windowEnd - windowStart + 1  # current window size
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if win_size == K :
            result.append(windowSum / K)  # calculate the average
            windowSum -= arr[windowStart]  # subtract the element going out
            windowStart += 1  # slide the window ahead

    return result


def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
