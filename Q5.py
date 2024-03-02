"""
Andrew Long 700716862
Write a function that accepts a string and calculate the number of upper-case letters and lower-case
letters.
Input String: 'The quick Brow Fox'
Expected Output:
No. of Upper-case characters: 3
No. of Lower-case Characters: 12
"""


# define function for counting cases
def case_count(x):
    # count variables
    upper_count = 0
    lower_count = 0

    # for loop in range of string
    for i in range(len(x)):
        # Use ASCII
        # if char is between 65-90 it is an uppercase
        if 65 <= ord(x[i]) <= 90:
            upper_count += 1
        # Use ASCII
        # if char is between 97-122 it is a lowercase
        elif 97 <= ord(x[i]) <= 122:
            lower_count += 1

    # print results
    print(f"No. of Upper-case characters: {upper_count}")
    print(f"No. of Lower-case characters: {lower_count}")


# define input
input_string = "The quick Brow Fox"

# print the input
print(f"The input string is: {input_string}")

# call function
case_count(input_string)
