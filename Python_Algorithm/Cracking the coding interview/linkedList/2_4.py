from LinkedList import LinkedList, Node


class divideLinkedList(LinkedList):
    # 2.4
    # N 기준으로 연결리스트 나누기
    def divideByN(self, N):
        A, B = LinkedList(), LinkedList()
        node = self.head.next
        while node != None:
            if node.data >= N:
                A.push(node.data)
            else:
                B.push(node.data)
            node = node.next
        B.getNode(B.length).next = A.head.next
        B.printList()


L = divideLinkedList()
L.push(3)
L.push(5)
L.push(1)
L.push(9)
L.push(2)
L.push(4)
L.printList()
L.divideByN(4)
