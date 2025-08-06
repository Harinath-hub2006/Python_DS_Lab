tup = []
sum_tup = []
n = int(input("Enter the number of elements: "))
for i in range(n):
        userInput = input(f"Enter the elements of tuple {i + 1} as comma seperated values: ")
        ele = tuple(map(int, userInput.split(',')))
        tup.append(ele)
for i in range(len(tup)):
        sum_of_list = sum(tup[i])
        sum_tup.append(sum_of_list)
print(sum_tup)

        
