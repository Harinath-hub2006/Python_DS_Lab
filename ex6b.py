class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is Empty")
        return self.queue.pop(0)
        
    def size(self):
        return len(self.queue)
    
def is_palindrome(x):
    obj = Queue()
    for char in x:
        obj.enqueue(char)
    while obj.size() > 1:
        if obj.dequeue() != obj.queue[-1]:
            return False
        obj.queue.pop()
    return True

s = input("Enter a palindrome: ")
if is_palindrome(s):
    print(f"The word {s} is a palindrome.")
else:
    print(f"The word {s} is not a palindrome.")
