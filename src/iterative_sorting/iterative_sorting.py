# TO-DO: Complete the selection_sort() function below

"""
    Separate the first element from the rest of the array. Think about it as a sorted list of one element.

    For all other indices, beginning with [1]:

    a. Copy the item at that index into a temp variable

    b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted
        Shift items over to the right as you iterate

    c. When the correct index is found, copy temp into this position
"""

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): ## starting at 1, len(arr)-1 starts at 1, because range is 0 or somethign of that nature
        cur_index = i ## temp variable
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
