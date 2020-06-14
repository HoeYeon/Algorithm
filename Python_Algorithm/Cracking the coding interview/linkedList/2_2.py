from LinkedList import LinkedList


class getKth(LinkedList):
    ## 2.2
    def getElement(self, k):
        count = 0
        node = self.head
        while count != self.length - k:
            node = node.next
            count += 1
        node.next = node.next.next


L = getKth()
L.push(1)
L.push(2)
L.push(3)
L.push(4)
L.push(5)
L.push(6)
L.printList()
L.getElement(2)
L.printList()
