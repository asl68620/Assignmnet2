"""
Long Andrew 700716862
Write a function that takes a list and returns a new list with unique items of the first list.
Sample List: [1,2,3,3,3,3,4,5]
Unique List: [1, 2, 3, 4, 5]
"""


def unique_lst(lst):
    # turn list into a set to remove duplicates
    lst = set(lst)

    # turn lst back to a list
    lst = list(lst)

    # return list
    return lst


# Sample List:
lst = [1, 2, 3, 3, 3, 3, 4, 5]
print(f"Original list: {lst}")

# call function and print
print(f"The unique list is: {unique_lst(lst)}")
