class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.di = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.di:
            return -1
        self.di.move_to_end(key)
        return self.di[key]

    def put(self, key: int, value: int) -> None:
        self.di[key] = value
        self.di.move_to_end(key)
        if len(self.di) > self.capacity:
            self.di.popitem(last=False)

