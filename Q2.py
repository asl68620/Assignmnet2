# 700716862 Andrew Long
"""
2. Use looping to output the elements from a provided list present at odd indexes.
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
"""

# generate my list
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# use for loop to scan through odd indexes
print("The odd indexes of my_list are: ", end='')
for i in range(len(my_list)):
    if i % 2 != 0:
        print(my_list[i], end=' ')
