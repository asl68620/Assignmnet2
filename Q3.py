"""
Andrew Long 700716862
Write a code that appends the type of elements from a given list.
Input
x = [23, ‘Python’, 23.98]
Expected output
[23, 'Python', 23.98]
[<class 'int'>, <class 'str'>, <class 'float'>]
"""

# initialize lst
x = [23, "python", 23.98]
type_lst = []

# for loop for len x
for i in range(len(x)):
    # append types into new list
    type_lst.append(type(x[i]))

# print both lists
print(f"list x is: {x}")
print(f"The types are: {type_lst}")
