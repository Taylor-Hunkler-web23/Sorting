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
            # print(arr)

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
       

#     a. Loop through elements on right-hand-side 
#     of current index and find the smallest element
        for right_side_element in range (cur_index, len(arr)):
            if arr[right_side_element] < arr [smallest_index]:
                smallest_index = right_side_element
             



        # TO-DO: swap
        # smallest_index should be swapped with cur_index

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]


    return arr

    




# 1. Loop through your array
#     - Compare each element to its neighbor
#     - If elements in wrong position (relative to each other, swap them)
# 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    

    swapped = True
    
    while swapped:
        # print(arr)
      

        swapped = False
    # 1. Loop through your array
        for i in range(0, len(arr) - 1):
           

        #     - Compare each element to its neighbor
            if arr[i] > arr[i +1]:

            #     - If elements in wrong position (relative to each other, swap them)

                arr [i], arr[i +1] = arr[i +1], arr[i]
            
           # 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
                swapped = True

                

                


    return arr


# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr