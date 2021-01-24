class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def find_sum(self):
        sum = self.data
        if self.left:
            sum += self.left.find_sum()
        if self.right:
            sum += self.right.find_sum()
        return sum

    def in_order_traversal(self):
        elements = []

        # traverse left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # add base node
        elements.append(self.data)

        # traverse right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        # traverse left subtree
        if self.left:
            elements += self.left.post_order_traversal()

        # traverse right subtree
        if self.right:
            elements += self.right.post_order_traversal()

        # add base node
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = []

        # add base node
        elements.append(self.data)

        # traverse left subtree
        if self.left:
            elements += self.left.pre_order_traversal()

        # traverse right subtree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True
        elif self.data < val:
            if self.right:
                return self.right.search(val)
            else:
                return False
        elif self.data > val:
            if self.left:
                return self.left.search(val)
            else:
                return False

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    nums = [42, 69, 420, 13, 59, 3, 9, 1337, 3, 9]
    nums_tree = build_tree(nums)
    print(nums_tree.in_order_traversal())
    print(nums_tree.search(1))
    print(nums_tree.search(1337))
    print(nums_tree.find_min())
    print(nums_tree.find_max())
    print(nums_tree.find_sum())
    nums2 = [5, 10, 4, 12, 3, 9, 6]
    nums_tree2 = build_tree(nums2)
    print(nums_tree2.find_sum())
    print(nums_tree2.in_order_traversal())
    print(nums_tree2.post_order_traversal())
    print(nums_tree2.pre_order_traversal())
