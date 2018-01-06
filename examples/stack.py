class Stack:
    def __init__(self):
        self.items = list()

    def empty(self):
        return self.items == list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]
