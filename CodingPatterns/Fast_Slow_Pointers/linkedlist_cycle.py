# Given the head of a Singly LinkedList, write a function to
# determine if the LinkedList has a cycle in it or not.
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    # TODO: Write your code here

    # slow and fast pointer
    slow = head
    fast = head

    # only iterate if there are at least 2 links after current
    while (slow.next and fast.next.next):

        slow = slow.next
        # fast "traverses" links faster
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))


main()
