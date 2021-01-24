class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        count = 0
        pt = self.parent
        while pt:
            count += 1
            pt = pt.parent
        return count

    def print_tree(self):
        indent = "  "*self.get_level() + ("|__" if self.get_level() > 0 else "")
        print(indent+self.data)
        if (len(self.children)) > 0:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Products")

    phones = TreeNode("Phones")
    phones.add_child(TreeNode("iPhone"))
    phones.add_child(TreeNode("Samsung"))
    phones.add_child(TreeNode("OnePlus"))

    laptops = TreeNode("Laptops")
    laptops.add_child(TreeNode("Asus"))
    laptops.add_child(TreeNode("Dell"))
    laptops.add_child(TreeNode("Acer"))

    root.add_child(phones)
    root.add_child(laptops)

    return root


if __name__ == "__main__":
    tree = build_product_tree()
    tree.print_tree()
    print(tree.get_level())
