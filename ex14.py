class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name

    def __str__(self):
        return f"Roll: {self.roll}, Name: {self.name}"


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, student):
        index = self.hash_function(student.roll)

        start = index
        while self.table[index] is not None and self.table[index].roll != student.roll:
            index = (index + 1) % self.size
            if index == start:
                print("Hash table full! Cannot insert.")
                return

        self.table[index] = student
        print("Student inserted successfully!")

    def search(self, roll):
        index = self.hash_function(roll)
        start = index
        while self.table[index] is not None:
            if self.table[index].roll == roll:
                print("Student found:", self.table[index])
                return
            index = (index + 1) % self.size
            if index == start:
                break
        print("Student not found.")

    def delete(self, roll):
        index = self.hash_function(roll)
        start = index
        while self.table[index] is not None:
            if self.table[index].roll == roll:
                print("Deleting record:", self.table[index])
                self.table[index] = None
                return
            index = (index + 1) % self.size
            if index == start:
                break
        print("Record not found.")

    def display(self):
        print("\n--- Hash Table ---")
        for i, record in enumerate(self.table):
            if record:
                print(f"Index {i}: {record}")
            else:
                print(f"Index {i}: Empty")

ht = HashTable(3)

# Insert students
ht.insert(Student(101, "Alice"))
ht.insert(Student(106, "Bob"))
ht.insert(Student(111, "Charlie"))

# Display hash table
ht.display()

# Search a student
ht.search(106)

# Delete a student
ht.delete(111)

# Display again after deletion
ht.display()

# Search for a deleted roll
ht.search(111)
