class HashTable:
    INITIAL_SIZE = 16

    def __init__(self):
        self.data = [0 for x in range(self.INITIAL_SIZE)]

    def put(self, key, value):
        index = self.get_index(key)
        entry = HashEntry(key, value)

        if not self.data[index]:
            self.data[index] = entry
        else:
            current_entry = self.data[index]

            while current_entry.next:
                current_entry = current_entry.next
            current_entry.next = entry

    def get(self, key):
        index = self.get_index(key)

        entry = self.data[index]
        if not entry.next:
            if entry.key == key:
                return entry.value
        else:
            while entry.next and entry.key != key:
                entry = entry.next
            if entry.key == key:
                return entry.value

    def get_index(self, key):
        return int(abs(hash(str(key))) % self.INITIAL_SIZE)

    def __str__(self):
        print(self.data)


class HashEntry:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
