class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(0)
        self.length = 0

    def push(self, data):
        node = self.head
        newNode = Node(data)
        while node.next != None:
            node = node.next
        newNode.next = node.next
        node.next = newNode
        self.length += 1

    def printList(self,):
        node = self.head
        while node.next != None:
            print(node.next.data, end=" -> ")
            node = node.next
        print()

    def getNode(self, n):
        node = self.head
        count = 0
        while count != n:
            node = node.next
            count += 1
        return node


# L = LinkedList()
# L.push(1)
# L.push(2)
# L.push(3)
# L.push(4)
# L.push(5)
# L.push(6)
# L.printList()
# L.printList()
