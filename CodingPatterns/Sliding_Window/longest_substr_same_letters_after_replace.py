# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter,
# find the length of the longest substring having the same letters after replacement.

def length_of_longest_substring(str1, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        max_repeat_letter_count = max(
            max_repeat_letter_count, frequency_map[right_char])

        # Current window size is from window_start to window_end, overall we have a letter which is
        # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
        # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
        # if the remaining letters are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' letters
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = str1[window_start]
            frequency_map[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == '__main__':
    str1 = "aabccbb"
    str2 = "abbcb"
    str3 = "aaabcdeeee"
    assert length_of_longest_substring(str1, 2) == 5
    assert length_of_longest_substring(str1, 1) == 3
    assert length_of_longest_substring(str2, 1) == 4
    assert length_of_longest_substring(str3, 1) == 5
