# Given a string, find the length of the longest substring, which has all distinct characters.

# Time: O(N)
# Space: O(26) = O(1)

def non_repeat_substring(str):
    # TODO: Write your code here
    winStart = 0
    # hashmap to keep track of characters' index
    char_indices = {}
    max_len = 0

    for winEnd in range(len(str)):

        # check if the character is unique or not
        if str[winEnd] in char_indices:
            # char is not unique (already has previous index)
            # shrink window to one position after the previous index 
            # ("get rid" of the previous copy of char)
            winStart = max(char_indices[str[winEnd]]+1, winStart)

        # char is unique
        # keep track of its index
        char_indices[str[winEnd]] = winEnd

        # all characters in window are unique
        winSize = winEnd - winStart + 1
        max_len = max(max_len, winSize)

    return max_len


if __name__ == '__main__':
    str1 = "aabccbb"  # 3
    str2 = "abbbb"  # 2
    str3 = "abccde"  # 3

    print(non_repeat_substring(str1))
    print(non_repeat_substring(str2))
    print(non_repeat_substring(str3))
