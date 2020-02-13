class Stack:
    def __init__(self):
        self.top = -1
        self.li = [0 for i in range(10)]
    
    def push(self,data):
        if self.top == 9:
            print('full')
            return
        self.top += 1
        self.li[self.top] = data
    
    def pop(self,):
        if len(self.li) == 0:
            print('error')
            return
        tmp = self.li[self.top]
        self.top -= 1
        return tmp

    def ttop(self):
        if len(self.li) == 0:
            print('error')
            return
        return self.li[self.top]

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())