class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.count = 0
        self.queue = deque()


    def get(self, key: int) -> int:
        if key not in self.map or self.map[key] == 0:
            return -1
        else:
            self.queue.append(key)
            ind = self.queue.index(key)
            del self.queue[ind]
            return self.map[key]

    def put(self, key: int, value: int) -> None:
        self.map[key] = value
        self.queue.append(key)
        self.count += 1
        if self.count > self.capacity:
            self.map[self.queue.popleft()] = 0
        print(self.queue)
        print(self.map)
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)