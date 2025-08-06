userInput = input("Enter elements of the list as comma seperated values: ")
list_of_ele = list(map(str, userInput.split(',')))
for i in range(len(list_of_ele)):
    for j in range(len(list_of_ele)):
        val = list_of_ele[i] + list_of_ele[j]
        print(val)
