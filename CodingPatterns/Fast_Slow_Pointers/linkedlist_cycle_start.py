# Given the head of a Singly LinkedList that contains a cycle,
# write a function to find the starting node of the cycle.

# Time: O(N)
# Space: O(1)

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    # TODO: Write your code here
    # find length of cycle
    len = find_cycle_len(head)
    ptr1 = head
    # increment ptr2 so that it is one cycle length away from ptr1
    ptr2 = head
    for i in range(len):
        ptr2 = ptr2.next

    while ptr1.next and ptr2.next:
        # where ptr1 and ptr2 meets, that is the start of the cycle
        # because ptr2 must have looped through the cycle back to the start
        if ptr1 == ptr2:
            break
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1


def find_cycle_len(head):
    slow = head
    fast = head
    # find where cycle happens
    while slow.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    # find length of cycle
    current = slow
    count = 0
    while current.next:
        # increment by one
        current = current.next
        count += 1
        if current == slow:
            break
    return count


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle length: " + str(find_cycle_len(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle length: " + str(find_cycle_len(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
