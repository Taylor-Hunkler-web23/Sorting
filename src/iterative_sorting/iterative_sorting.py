# TO-DO: Complete the selection_sort() function below 

# 1. Start with current index = 0

# 2. For all indices EXCEPT the last index:

#     a. Loop through elements on right-hand-side 
#     of current index and find the smallest element

#     b. Swap the element at current index with the
#     smallest element found in above loop


def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
       

# loop through array starting after cur_index 
        for right_side_element in range (cur_index, len(arr)):
            if arr[right_side_element] < arr [smallest_index]:
                smallest_index = right_side_element
             



        # TO-DO: swap
        # smallest_index should be swapped with cur_index

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]


    return arr
    


# TO-DO:  implement the Bubble Sort function below
# def bubble_sort( arr ):

#     return arr


# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr