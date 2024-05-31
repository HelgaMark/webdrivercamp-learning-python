#!/usr/bin/python3

my_list = [5, 4, 3, 2, 1]

# ADD YOUR CODE HERE

result = []

for i in my_list:
    #if is even
    if i % 2 == 0:
        result.append(True)

    else:
        result.append(False)

even_odd_tuple = tuple(result)

print(my_list)
print(even_odd_tuple)

