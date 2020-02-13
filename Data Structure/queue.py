class Queue:
    def __init__(self,):
        self.front = -1
        self.back = -1
        self.li = [0 for i in range(3)]
    
    def push(self, data):
        if abs(self.back - self.front) == 3:
            print('full of queue')
            return
        self.back = (self.back+1)%3
        self.li[self.back] = data

    def dequeue(self,):
        if self.back == self.front:
            return 'cant dequeue'
        self.front = (self.front+1)%3
        return self.li[self.front]
    
    def ttop(self):
        if self.back == self.front:
            return 'error'
        return self.li[(self.front+1)%3]
q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q.dequeue())
print(q.ttop())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.ttop())
q.push(4)
print(q.ttop())