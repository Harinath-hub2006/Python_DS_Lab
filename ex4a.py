class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self, item):
        if self.isEmpty():
            raise IndexError("Queue is Empty")
        return self.queue.pop(0)

    def printQueue(self):
        i = 0
        for i in range(len(self.queue)):
            print(self.queue[i])

    def peek(self):
         if self.isEmpty():
            raise IndexError("Queue is Empty")
         return self.queue[0]

    def size(self):
        return len(self.queue)

obj = Queue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
print("Queue after enqueue: ")
obj.printQueue()
obj.dequeue(1)
print("Queue after dequeue: ")
obj.printQueue()
obj.peek()
print("Queue front: ",obj.peek())
print("Queue size: ",obj.size())
