## make queue using 2 stacks

from LinkedListStack import LinkedListStack


class MyQueue(LinkedListStack):
    def __init__(self):
        self.s1 = LinkedListStack()
        self.s2 = LinkedListStack()

    def enqueue(self, data):
        self.s1.push(data)

    def dequeue(self):
        if self.s2.size != 0:
            return self.s2.pop()
        while self.s1.size != 0:
            self.s2.push(self.s1.pop())
        return self.s2.pop()


queue = MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(82)
queue.enqueue(7)
queue.enqueue(93)
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(54)
print(queue.dequeue())
queue.enqueue(999)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
