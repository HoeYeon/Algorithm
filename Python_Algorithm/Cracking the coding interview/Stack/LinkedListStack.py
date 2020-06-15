class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.top = Node()
        self.size = 0

    def push(self, data):
        node = Node()
        node.data = data
        node.next = self.top.next
        self.top.next = node
        self.size += 1

    def pop(self):
        data = self.top.next.data
        self.top.next = self.top.next.next
        self.size -= 1
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
