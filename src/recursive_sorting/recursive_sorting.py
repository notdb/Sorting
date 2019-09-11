# TO-DO: complete the helpe function below to merge 2 sorted arrays
arr1 = [0,1,2,3,4,5,6,7,8]
arrA = [0,1,2,3,4,5,6,7,8]
arrB = [9]



def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    newArr = []
    print(len(merged_arr))
    # we know the length of what the final array should be and we know the sizes of the two arrays also have to add up to the length of the final array. we can grab the length of the two smaller arrays. we know the smaller array will always be on the right. if array 1 is empty, two goes on the end, if array 2 is empty 1 goes on the end
    for i in range(len(merged_arr)):
        print(i)
        print(f"{len(arrA)} BBBBBBBARSTARST")
        print(f"{len(arrB)} AAAAAAAAAAarstarst")
        if len(arrA) == 0 and len(arrB) > 1:
            newArr.append(arrB.pop(0))
        elif len(arrA) == 0:
            newArr.append(arrB.pop())
            print('A DING')
            print(newArr)
            return newArr
        elif len(arrB) == 0:
            newArr.append(arrA.pop())
            print('B DING')
            print(newArr)
            return newArr
        elif arrA[0] > arrB[0]:
            newArr.append(arrB.pop(0))
        else:
            newArr.append(arrA.pop(0))
        print(newArr)
    print(merged_arr)
    print(newArr)

#merge(arrA, arrB)
# TO-DO: implement the Merge Sort function below USING RECURSION
"""
It's two steps, breaking apart until a sorted array, and then merging until you have a final array

"""
    
def merge_sort(arr):
    splitArrays = []
    garbageCollector = []
    sortedArray = []
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
                  #  print(i)
                  #  print(splitArrays)
                  #  print(f"{len(arr[i][:newArr])} + {arr[i][:newArr]} AWYARSTINARST")
                    if len(arr[i][:newArr]) == 0:
                        garbageCollector.append(arr[i][:newArr])
                    else:
                        splitArrays.append(arr[i][:newArr])
                  #  print(f"{i} aaa")
                  #  print(splitArrays)
                    splitArrays.append(arr[i][newArr:])
                  #  print(splitArrays)
               
   
   
   
    if len(splitArrays) >= len(arr1):
      #  print(len(arr1) % 2)
        while len(splitArrays[0]) is not len(arr1):
            print(len(sortedArray))
            print(f"{len(splitArrays)} ARTARSTARSTARST")
            if len(splitArrays) % 2 == 0:
                for i in range(len(splitArrays)//2):
                    print(f"{splitArrays} CCCCCCCCCCCCCCCC")
                   # if len(splitArrays) == 1:
                    #    splitArrays.append(splitArrays.pop(0))
                   # else:
                    splitArrays.append(merge(splitArrays.pop(0),splitArrays.pop(0)))
                   
            else:
                for i in range(len(splitArrays)//2 + 1):
                    if len(splitArrays) == 1:
                        print(f"{splitArrays} TEST HERE")
                        splitArrays.append(splitArrays.pop(0))
                    else:
                        splitArrays.append(merge(splitArrays.pop(0),splitArrays.pop(0)))
                
            print(f"{splitArrays} bbbbbbbbbbb")
                        
        return splitArrays[0]
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
