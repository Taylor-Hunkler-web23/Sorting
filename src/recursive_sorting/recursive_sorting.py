# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element 
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled
# ```

# visual test
# arrA[1x, 3x, 8] left_elem=2
# arrB[2x, 7x] right_elem =2
# i count=0,1,2,3,4
# merged_arr[1, 2, 3, 7]


# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

#array indexes
    left_elem= 0
    right_elem= 0
    

    # TO-DO
    for i in range(elements):

        #if at the end of arrA
        if len(arrA) <= left_elem:
            merged_arr[i] = arrB[right_elem]
            right_elem +=1
            
            #if at the end of arrB
        elif len(arrB) <= right_elem:
            merged_arr[i] = arrA[left_elem]
            left_elem +=1
            
 # if the element in the left array is smaller than the element in the right array, then put the left array element into the merged array. Increment index
        elif arrA[left_elem] < arrB[right_elem]:
            merged_arr[i]= arrA[left_elem]
            left_elem += 1

         # else- the right array element is smaller, so put that into the merged array. Increment index
        else:
            merged_arr[i]= arrB[right_elem]
            right_elem +=1
    print (merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
     
    
# 1. While your data set contains more than one item, split it in half
    if len(arr)> 1:
        left_arr = arr[:len(arr) // 2] 
        right_arr = arr[len(arr) // 2:]


# keep sorting in half with recursion
        left_arr = merge_sort(left_arr)
        right_arr = merge_sort(right_arr)

    # use helper function to merge sorted arrays back together
        return merge(left_arr, right_arr)

    return arr


# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
