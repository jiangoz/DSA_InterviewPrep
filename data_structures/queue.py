from collections import deque

# implemented using deque


class Queue:

    def __init__(self):
        self.container = deque()

    def enqueue(self, val):
        self.container.appendleft(val)

    def dequeue(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
