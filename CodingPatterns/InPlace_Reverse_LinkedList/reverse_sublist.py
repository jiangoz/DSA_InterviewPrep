# Given the head of a LinkedList and two positions ‘p’ and ‘q’,
# reverse the LinkedList from position ‘p’ to ‘q’

# Time: O(N)
# Space: O(1)

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_sub_list(head, p, q):
    # TODO: Write your code here

    # no range to reverse
    if p == q:
        return head

    i = 1  # position of node, start at 1st node
    current, resHead = head, head
    node_before_sublist = None
    while current and i < p:
        node_before_sublist = current
        current = current.next
        i += 1

    # current is at the pth node

    prev, sublist_tail = current, current
    # reverse until we reach qth node
    while current and i <= q:
        tmpNext = current.next
        current.next = prev
        prev = current
        current = tmpNext
        i += 1

    # current is at (q+1)th node
    sublist_tail.next = current

    # prev is at head of sublist

    if node_before_sublist:
        node_before_sublist.next = prev
        return resHead
    # there was no node before sublist, so prev is the 1st node in result
    else:
        return prev


def main():

    for p in range(1, 6):
        for q in range(p, 6):

            head = Node(1)
            head.next = Node(2)
            head.next.next = Node(3)
            head.next.next.next = Node(4)
            head.next.next.next.next = Node(5)

            print("Nodes of original LinkedList are: ", end='')
            head.print_list()

            result = reverse_sub_list(head, p, q)
            print(f"Reversing node {p} to {q}: ", end='')
            result.print_list()


main()
