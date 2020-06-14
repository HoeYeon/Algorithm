from LinkedList import LinkedList


def getNum(L):
    num = 0
    start = 0
    node = L.head.next
    while node != None:
        num += 10 ** start * node.data
        start += 1
        node = node.next
    return num


def setLinkedList(num):
    L = LinkedList()
    while num != 0:
        L.push(num % 10)
        num //= 10
    return L


L = LinkedList()
L2 = LinkedList()
L.push(3)
L.push(5)
L.push(1)
L2.push(9)
L2.push(2)
L2.push(4)
L.printList()
print(getNum(L))
L2.printList()
print(getNum(L2))
L3 = setLinkedList(getNum(L) + getNum(L2))
L3.printList()
