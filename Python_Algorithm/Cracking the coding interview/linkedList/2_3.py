from LinkedList import LinkedList


class deleteNode(LinkedList):
    # 2.3
    # 현재 노드에 다음 노드 값 복사 & 다음 노드 삭제
    # 마지막 노드의 경우 삭제못함
    def deleteCurrentNode(self, n):
        node = n
        node.data = node.next.data
        node.next = node.next.next


L = deleteNode()
L.push(1)
L.push(2)
L.push(3)
L.push(4)
L.push(5)
L.push(6)
L.printList()
L.deleteCurrentNode(L.getNode(3))
L.printList()
