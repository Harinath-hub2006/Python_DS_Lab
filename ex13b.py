def bubble_sort(marks):
    n = len(marks)
    arr = marks.copy() 
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
    return arr

def insertion_sort(marks):
    arr = marks.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(marks):
    arr = marks.copy()
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  
    return arr

n = int(input("Enter number of students: "))

marks = []
for i in range(n):
    m = float(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

print("\nOriginal Marks:", marks)

print("\n--- Sorted Marks (Ascending Order) ---")
print("Using Bubble Sort   :", bubble_sort(marks))
print("Using Insertion Sort:", insertion_sorted)
print("Using Selection Sort:", selection_sorted)
