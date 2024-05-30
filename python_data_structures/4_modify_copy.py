#!/usr/bin/python3

#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5

modified_list = list_[:]

if index >= 0 and index < len(modified_list):
    modified_list[index] = element_to_replace

print("Copy:      ", modified_list)
print("Original:  ", list_)

