class Node:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.head = None

    def djb2(self, key):
        # research later to get better understanding
        # hash = 5381
        # for x in key:
        #     hash = ((hash << 5) + hash) + ord(x)
        # return hash & 0xFFFFFFFF
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        index = self.hash_index(key)

        self.storage[index] = Node(key, value)

        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """


table = HashTable()

table.put("hello", 5)
table.put("woooooooop", 1525125)


print(table.storage[4].next)
