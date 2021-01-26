# Given a string, find the length of the longest substring in it
# with no more than K distinct characters.


# Solution 1: using list to "remember" if element is distinct
def longest_substring_with_k_distinct(str, k):
    # TODO: Write your code here
    #str = list(str)
    longest_substring_len = 0
    distinct_char_count = 0
    win_list = [] # for "remembering"
    for win_end in range(len(str)):

        #prev_distinct_char_count = distinct_char_count

        # check if incoming character is distinct
        if str[win_end] not in win_list:
            distinct_char_count += 1

        win_list.append(str[win_end])  # append incoming element

        # if current distinct count is no more than k
        if distinct_char_count <= k:
            longest_substring_len = max(longest_substring_len, len(win_list))

        # if distinct count is more than k
        while distinct_char_count > k:
            # shrink window (left bound)
            left_element = win_list[0]
            # if element is not found in "remember" list, we lost a distinct element
            win_list.pop(0)
            if left_element not in win_list:
                distinct_char_count -= 1

    return longest_substring_len


# Solution 2: using hashmap/dict to "remember"
def longest_substring_with_k_distinct_hash(str1, k):
    window_start = 0
    max_length = 0
    char_frequency = {} # for "remembering"

    # in the following loop we'll try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
        while len(char_frequency) > k:
            left_char = str1[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1  # shrink the window
        # remember the maximum length so far
        max_length = max(max_length, window_end-window_start + 1)
    return max_length


if __name__ == "__main__":
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("cbbebi", 3)))

    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("adsgsadf", 1)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("xcfgsdf", 3)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("casdggw", 2)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("dddddddd", 1)))

    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct_hash("araaci", 2)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct_hash("araaci", 1)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct_hash("cbbebi", 3)))
