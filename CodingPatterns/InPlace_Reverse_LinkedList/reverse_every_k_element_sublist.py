# Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.
# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

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


def reverse_every_k_elements(head, k):
    # TODO: Write your code here

    # base cases
    if not head or k <= 1:
        return head

    current = head
    prev = None
    resHead = None

    while True:

        # originally the first node of non-reversed sublist
        last_node_of_current_sublist = current

        last_node_of_prev_sublist = prev
        # new/next batch of nodes to reverse
        i = 0

        # reverse the nodes
        while current and i < k:
            tmpNext = current.next
            current.next = prev
            prev = current
            current = tmpNext
            i += 1

        # prev is now head of current reversed sublist
        if last_node_of_prev_sublist:
            # connect previous sublist with current reversed sublist
            last_node_of_prev_sublist.next = prev
        else:
            # this is the first reversed sublist; its head will be returned result
            resHead = prev

        # current is now at the "next" node
        # connect current sublist with next/current
        last_node_of_current_sublist.next = current

        # update the previous node
        prev = last_node_of_current_sublist

        # break loop to return result
        if not current:
            break

    return resHead


def main():

    for i in range(8):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        head.next.next.next.next.next.next = Node(7)
        head.next.next.next.next.next.next.next = Node(8)

        print("Nodes of original LinkedList are: ", end='')
        head.print_list()
        result = reverse_every_k_elements(head, i)
        print(f"k = {i} Nodes of reversed LinkedList are: ", end='')
        result.print_list()


main()
