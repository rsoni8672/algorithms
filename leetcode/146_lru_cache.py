class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_capacity = 0
        self.sequence = []
        self.map = {}

    def get(self, key: int) -> int:
        index = 0
        if key not in self.sequence:
            return -1
        self.sequence.remove(key)
        self.sequence.append(key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        index = 0

        if key in self.sequence:
            self.sequence.remove(key)
            self.sequence.append(key)
        else:
            self.sequence.append(key)
            if len(self.sequence) > self.capacity:
                self.map.pop(self.sequence[0])
                self.sequence = self.sequence[1:]
        self.map[key] = value



    # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == "__main__":
    operations = ["LRUCache","put","put","get","put","put","get"]

    values = [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
    solution = LRUCache(values[0][0])

    for index in range(1, len(operations)):
        if operations[index] == "put":
            solution.put(values[index][0], values[index][1])
        else:
            print(solution.get(values[index][0]))
