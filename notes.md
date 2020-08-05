## Collision resolution by chaining

Make our array of slots into an array of linked lists.
Each linked list node is a HashTableEntry.
Put

---

Slot
Index Chain (linked list)

---

0 -> None
1 {foo:12} -> None
2 {baz:999} -> {bar:50} -> None
3 -> None

put("foo", 12) # hashes to 1
put("bar", 30) # hashes to 2
put("baz", 999) # hashes to 2 -- collision
put("bar", 50) # hashes to 2 -- collision

1. Figure out the index
2. Search the linked list to see if the key is there
   2a. If the key is there, overwrite the value
   2b. If not there, create a new HashTableEntry and insert it in the list
   Get

---

1. Figure out the index for the key
2. Search the linked list at the index for the HashTableEntry that matches the key
3. Return the value for the entry, or None if not found
   Delete

---

1. Figure out the index for the key
2. Search the linked list at the index for the HashTableEntry that matches the key
   2a. If found, delete the entry from the linked list--return the value
   2b. If not found, return None

class Node:
def **init**(self, value):
self.value = value
self.next = None
​
def **repr**(self):
return f'Node({repr(self.value)})'
​
class LinkedList:
def **init**(self):
self.head = None
​
def **str**(self):
"""Print entire linked list."""
​
if self.head is None:
return "[Empty List]"
​
cur = self.head
s = ""
​
while cur != None:
s += f'({cur.value})'
​
if cur.next is not None:
s += '-->'
​
cur = cur.next
​
return s
​
def find(self, value):
cur = self.head
​
while cur is not None:
if cur.value == value:
return cur
​
cur = cur.next
​
return None
​
def delete(self, value):
cur = self.head
​ # Special case of deleting head
​
if cur.value == value:
self.head = cur.next
return cur
​ # General case of deleting internal node
​
prev = cur
cur = cur.next
​
while cur is not None:
if cur.value == value: # Found it!
prev.next = cur.next # Cut it out
return cur # Return deleted node
else:
prev = cur
cur = cur.next
​
return None # If we got here, nothing found
​
def insert_at_head(self, node):
node.next = self.head
self.head = node
​
def insert_or_overwrite_value(self, value):
node = self.find(value)
​
if node is None: # Make a new node
self.insert_at_head(Node(value))
​
else: # Overwrite old value
node.value = value
