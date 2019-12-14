import sys

class Queue:
    def __init__(self):
        self.front = 0
        self.back = 0
        self.size = 0
        self.li = []

    def ssize(self):
        return self.size

    def empty(self):
        return 1 if self.size == 0 else 0

    def push(self, data):
        #self.li[self.back] = data
        self.back += 1
        self.size += 1
        self.li.append(data)

    def pop(self):
        if self.empty():
            return -1
        tmp = self.li[self.front]
        self.front += 1
        self.size -= 1
        return tmp

    def ffront(self):
        return -1 if self.empty() else self.li[self.front]

    def bback(self):
        return -1 if self.empty() else self.li[self.back-1]


q = Queue()
n=int(sys.stdin.readline())
for i in range(n):
    s=sys.stdin.readline()
    s=s.strip()
    s=s.split(' ')
    if s[0] == 'push':
        q.push(s[1])
    elif s[0] == 'pop':
        print(q.pop())
    elif s[0] == 'empty':
        print(q.empty())
    elif s[0] == 'size':
        print(q.ssize())
    elif s[0] == 'front':
        print(q.ffront())
    elif s[0] == 'back':
        print(q.bback())
