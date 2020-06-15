class ArrayStack:
    def __init__(self):
        self.top = -1
        self.size = 100
        self.stack = [0 for i in range(self.size)]

    def push(self, data):
        self.top += 1
        self.stack[self.top] = data

    def pop(self,):
        data = self.stack[self.top]
        self.top -= 1
        return data

    def getTop(self):
        return self.stack[self.top]


# s = ArrayStack()
# s.push(1)
# s.push(2)
# s.push(3)
# print(s.getTop())
# print(s.pop())
# print(s.getTop())
# s.push(5)
# print(s.getTop())
