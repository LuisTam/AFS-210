class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]


def isPalindrome(s):
    # Create instances of Stack and Queue
    stack = Stack()
    queue = Queue()

    # Enqueue and push characters from the string
    for char in s:
        if char.isalpha():
            char = char.lower()  # Ignore case
            queue.enqueue(char)
            stack.push(char)

    # Dequeue and pop characters and check for palindrome
    while not stack.isEmpty() and not queue.isEmpty():
        if stack.pop() != queue.dequeue():
            return False

    return True


# Test the isPalindrome function
strings_to_test = ["racecar", "noon", "python", "madam"]

for s in strings_to_test:
    result = isPalindrome(s)
    print(f"{s} is a palindrome: {result}")
