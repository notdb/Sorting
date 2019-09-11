# TO-DO: Complete the selection_sort() function below

"""
Start with current index = 0

For all indices EXCEPT the last index:

a. Loop through elements on right-hand-side of current index and find the smallest element

b. Swap the element at current index with the smallest element found in above loop

"""

arr = [1,8,4,5,6,2,3]
def selection_sort(arr):
    # loop through n-1 elements
   swapped = True
   
   while swapped is True:
    for i in range(0, len(arr) - 1):
        cur_index = i
       # print(f"{cur_index} + a")
        smallest_index = cur_index
       # print(f"{smallest_index} + b")
        temp = arr[cur_index]
        print(f"{temp} + BBB")
        print(f"{arr[cur_index]} + ccc")
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        """
        if arr[cur_index] > arr[cur_index+1]:
            temp = arr[cur_index]
            arr[cur_index] = arr[cur_index+1]
            arr[cur_index+1] = temp
        """
        if arr[cur_index] > arr[cur_index+1]:
            swapped = True
            temp = arr[cur_index] # this needs to not change
            
           # arr[cur_index] = temp
            print(f"{temp} + AAA")
            print(f"{arr[cur_index]} + TESTING VAR 1")
            print(f"{arr[cur_index+1]} + TESTING VAR 2")
        else:
            swapped = False
        # TO-DO: swap
        
    return arr


keyTimes = [[0,2], [1,5], [0,9], [2,15]]
keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def slowestKey(keyTimes):
    emptyList = []
    emptyList2 = []
    for a in keyTimes:
        print(a[1])
        b = int(a[1])
        emptyList.append(b)

    emptyList.pop()
    emptyList.insert(0, 0)
    print(emptyList)
    for a in keyTimes:
        print(a[1])
        b = int(a[1])
        emptyList2.append(b)

    print(emptyList2)
    newList = []
    for a in range(0, len(emptyList)):
       
        newList.append(emptyList2[a]-emptyList[a])

    newList.sort()
    combinedList = []
    for a in range(0, len(keys)):
        combinedList.append([newList[a],keys[a]])
    print(newList)
    print(combinedList)
        
print(slowestKey(keyTimes))
   
print("hello world")
print(selection_sort(arr))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
