# 700716862 Andrew Long
# Use a python code to display the following star pattern using the for loop

# variable for second half of pyramid
j = 4

# for loop for printing each row
for i in range(10):
    # if first half of pyramid print i number of '*'
    if i < 6:
        print('* ' * i )
    # if second half print j number of '*'
    else:
        print('* ' * j)
        # decrement j by 1
        j = j - 1