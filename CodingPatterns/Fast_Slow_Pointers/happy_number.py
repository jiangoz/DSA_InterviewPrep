# Any number will be called a happy number if, after repeatedly replacing it
# with a number equal to the sum of the square of all of its digits,
# leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’.
# Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

# Time: O(log(N))
# Space: O(1)

def find_happy_number(num):
    # TODO: Write your code here

    # fast and slow pointer/calculator
    fast = num
    slow = num

    while True:
        slow = happy_sum(slow)
        fast = happy_sum(happy_sum(fast))

        # reached 1; must be happy
        if slow == 1:
            return True

        # pointers met; there is a cycle that doesn't include 1
        if slow == fast:
            return False

# calculate the "happy" sum of a number
# sum of the square of all its digits


def happy_sum(num):
    sum = 0
    for digit in str(num):
        sum += int(digit) ** 2
    return sum


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))
    assert happy_sum(23) == 13
    assert happy_sum(13) == 10
    assert happy_sum(10) == 1


main()
