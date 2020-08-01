# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import OrderedDict


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.d = OrderedDict()

    def setPrior(self, key, value):
        self.d[key] = value
        self.d.move_to_end(key)
        if len(self.d) > self.capacity:
            self.d.popitem(last=False)

    def printItem(self):
        ans = ""
        for i in reversed(self.d.values()):
            ans += str(i) + " "
        print(ans)


banks = list(input().split())
lru = LRU(5)
for i in banks:
    lru.setPrior(i, i)
    lru.printItem()

