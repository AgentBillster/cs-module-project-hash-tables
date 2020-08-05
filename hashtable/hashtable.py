class Node:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def add_or_replace(self, key, value):

        while self.head is not None:

            if self.head.key == key:
                self.head.value = value
            self.head = self.head.next

        newNode = Node(key, value)
        newNode.next = self.head
        self.head = newNode


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

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.storage

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        # perhaps later research this
        pass

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
        newList = LinkedList(Node(key, value))

        if self.storage[index] == None:
            self.storage[index] = newList
        else:
            self.storage[index].add_or_replace(key, value)

        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

    def delete(self, key):
        """day one"""
        if self.storage[self.hash_index(key)] == None:
            print("DOES NOT EXIST")

        else:
            self.storage[self.hash_index(key)] = None

        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

    def get(self, key):
        if self.storage[self.hash_index(key)] == None:
            print("DOES NOT EXIST")

        else:
            return self.storage[self.hash_index(key)]

    """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
    """

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")


tab = HashTable()

print(tab.storage)  # INITIAL EMPTY ARRAY
tab.put("billy", 24)
tab.put("harper", 7)
print(tab.storage)  # with family names and ages

print(tab.get('billy'))
print(tab.get('harper'))  # gets specific item


tab.delete("billy")
tab.delete("billy2222")
tab.delete("harper")

print(tab.storage)
