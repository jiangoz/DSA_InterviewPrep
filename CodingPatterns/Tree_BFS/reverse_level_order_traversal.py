# Given a binary tree, populate an array to represent its level-by-level traversal in reverse order,
# i.e., the lowest level comes first. You should populate the values of all nodes in each level
# from left to right in separate sub-arrays.

# Time: O(N)
# Space: O(N)

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    if not root:
        return []

    result = deque()

    queue = deque()
    queue.append(root)

    while queue:

        levelSize = len(queue)
        levelVals = []

        for _ in range(levelSize):
            node = queue.popleft()
            levelVals.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # insert at front (reverse order)
        result.appendleft(levelVals)

    return list(result)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
