class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count

    def addFirst(self, data) -> None:
        # Add a node at the front of the list
        new_node = Node(data)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node

        self.head = new_node
        self.count += 1

    def addLast(self, data) -> None:
        # Add a node at the end of the list
        new_node = Node(data)

        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        else:
            self.head = new_node

        self.tail = new_node
        self.count += 1

    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.
        if index > self.count:
            return
        if index == 0:
            self.addFirst(data)
            return
        if index == self.count:
            self.addLast(data)
            return

        new_node = Node(data)
        curr = self.head
        for _ in range(index):
            curr = curr.next

        new_node.prev = curr.prev
        new_node.next = curr
        curr.prev.next = new_node
        curr.prev = new_node
        self.count += 1

    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

# Create the Doubly Linked List
words = DoublyLinkedList()
words.addLast("May")
words.addLast("the")
words.addLast("Force")
words.addLast("be")
words.addLast("with")
words.addLast("you")
words.addLast("!")

# Print the list
print(list(words))

# Return the index position of "with" in the list and print this value
index_of_with = words.indexOf("with")
print("Index of 'with':", index_of_with)

# Change "you" into "us" on the list
words.__setitem__(5, "us")

# Add "all" before "!" on the list
words.addAtIndex("all", words.size() - 1)

# Print the modified list
print(list(words))
