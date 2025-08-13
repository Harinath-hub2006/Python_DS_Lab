class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def sizeOfQueue(self):
        return self.length

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = self.head = new_node
            self.length += 1
            return
        current = self.tail
        while current.next:
            current = current.next
        current.next = new_node
        self.tail = new_node
        self.length += 1
        

    def dequeue(self, data):
        if self.isEmpty():
            return "Queue is Empty"
        temp = self.head.data
        self.head = self.head.next
        self.length -= 1
        if self.head is None:
            self.tail = None
        return temp

    def peek(self):
         if self.isEmpty():
             return "Queue is empty"
         return self.head.data

    def printQueue(self):
        temp = self.head
        while temp:
          print(temp.data, end=" -> ")
          temp = temp.next
        print()

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue after enqueue: ")
queue.printQueue()
print("Length of the queue: ",queue.sizeOfQueue())
print("Element dequeued: ",queue.dequeue(1))
print("Queue after dequeue: ")
queue.printQueue()
print("Peek: ",queue.peek())
print("Length of the queue: ",queue.sizeOfQueue())

        
        
        
