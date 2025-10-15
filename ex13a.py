def linear_search(rolls, key):
    for i in range(len(rolls)):
        if rolls[i] == key:
            return True
    return False

def binary_search(rolls, key):
    low = 0
    high = len(rolls) - 1

    while low <= high:
        mid = (low + high) // 2
        if rolls[mid] == key:
            return True
        elif rolls[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False

n = int(input("Enter number of registered students: "))

rolls = []
for i in range(n):
    r = int(input(f"Enter roll number {i+1}: "))
    rolls.append(r)

rolls.sort()
print("\nSorted roll numbers:", rolls)

key = int(input("\nEnter roll number to verify registration: "))

found_linear = linear_search(rolls, key)
if found_linear:
    print(f"Linear Search: Student {key} is registered for the exam.")
else:
    print(f"Linear Search: Student {key} is NOT registered for the exam.")

found_binary = binary_search(rolls, key)
if found_binary:
    print(f"Binary Search: Student {key} is registered for the exam.")
else:
    print(f"Binary Search: Student {key} is NOT registered for the exam.")
