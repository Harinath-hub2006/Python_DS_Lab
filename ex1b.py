dict_of_ele = {'x' : ["a", "b", "c"], 'y' : ["d", "e", "f"]}
for i in dict_of_ele['x']:
    for j in dict_of_ele['y']:
        val = i + j
        print(val)
        print(val[-1:] + val[:-1])
