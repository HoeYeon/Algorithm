class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.top = Node()

    def push(self, data):
        node = Node()
        node.data = data
        node.next = self.top.next
        self.top.next = node

    def pop(self):
        data = self.top.next.data
        self.top.next = self.top.next.next
        return data

    def getTop(self):
        return self.top.next.data


# s = LinkedListStack()
# s.push(1)
# s.push(2)
# s.push(3)
# print(s.getTop())
# print(s.pop())
# print(s.getTop())
# s.push(5)
# print(s.getTop())
