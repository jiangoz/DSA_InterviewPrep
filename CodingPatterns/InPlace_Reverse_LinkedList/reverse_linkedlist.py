# Given the head of a Singly LinkedList, reverse the LinkedList.
# Write a function to return the new head of the reversed LinkedList.

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


def reverse(head):
    previous = None
    while head:
        next = head.next  # temporarily store the next node
        head.next = previous  # reverse the current node
        previous = head  # before we move to the next node, point previous to the current node
        head = next  # move onto the next node
    return previous


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
