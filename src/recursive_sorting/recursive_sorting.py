# TO-DO: complete the helpe function below to merge 2 sorted arrays
arr1 = [3,5,6,4,1,7,9]
arrA = [8,2]
arrB = [3]



def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
 

# TO-DO: implement the Merge Sort function below USING RECURSION
"""
It's two steps, breaking apart until a sorted array, and then merging until you have a final array

"""
    
def merge_sort(arr):
    splitArrays = []
    garbageCollector = []
    # way to save the original array length to know when to stop
    # splitting the array
    if type(arr[0]) is int:
        newArr = len(arr) // 2
        splitArrays.append(arr[:newArr])
        splitArrays.append(arr[newArr:])
    else:
        if arr[0] is None:
            return 0
        else:
            for i in range(len(arr)):
                   
                    newArr = len(arr[i]) // 2
                    print(i)
                    print(splitArrays)
                    print(f"{len(arr[i][:newArr])} + {arr[i][:newArr]} AWYARSTINARST")
                    if len(arr[i][:newArr]) == 0:
                        garbageCollector.append(arr[i][:newArr])
                    else:
                        splitArrays.append(arr[i][:newArr])
                    print(f"{i} aaa")
                    print(splitArrays)
                    splitArrays.append(arr[i][newArr:])
                    print(splitArrays)
               
   
   
   
    if len(splitArrays) >= len(arr1):
        print(len(arr1) % 2)
        return splitArrays
    else:
       merge_sort(splitArrays)
      
    
merge_sort(arr1)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
