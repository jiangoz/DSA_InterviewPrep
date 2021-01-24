class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head, None)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                itr.next = node
                return
            itr = itr.next
        print(data_after + " is not in the linked list")

    def contains(self, data):
        itr = self.head
        while itr:
            if itr.data == data:
                return True
            itr = itr.next
        return False

    def remove_by_value(self, data):
        # Remove first node that contains data

        if not self.contains(data):
            print(data + " is not in linked list")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next

    def print_forward(self):
        # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("empty list")
        output = ""
        itr = self.head
        while itr:
            output += (itr.data + "-->") if itr.next else itr.data
            itr = itr.next
        print(output)

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            print("empty list")

        itr = self.head
        while itr:
            if itr.next is None:
                break
            itr = itr.next

        out = ""
        while itr:
            out += (itr.data + ">>") if itr.prev else itr.data
            itr = itr.prev
        print(out)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
    ll.insert_after_value("mango", "apple")
    ll.insert_at(0, "haha")
    ll.print()
    ll.insert_after_value("haha", "lol")
    ll.print()
    ll.insert_at_begining("xd")
    ll.insert_at_end("kek")
    ll.print()
    ll.remove_at(1)
    ll.print()
    ll.remove_by_value("xd")
    ll.print()
    print(ll.contains("kek"))
    ll.insert_after_value("lol", "bruh")
    ll.print()
    ll.print_forward()
    ll.print_backward()
    ll2 = DoublyLinkedList()
    ll2.insert_values(["banana", "mango", "grapes", "orange"])
    ll2.print_forward()
    ll2.print_backward()
