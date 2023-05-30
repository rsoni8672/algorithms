class MyHashSet:

    def __init__(self):
        self.dummy_set = []

    def add(self, key: int) -> None:
        if len(self.dummy_set) == 0:
            self.dummy_set.append(key)
        else:
            if key > self.dummy_set[-1]:
                self.dummy_set.append(key)
                return
            for index in range(len(self.dummy_set)):
                if key == self.dummy_set[index]:
                    return
                if key < self.dummy_set[index]:
                    self.dummy_set.insert(index, key)
                    break

    def remove(self, key: int) -> None:
        if key in self.dummy_set:
            self.dummy_set.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.dummy_set
