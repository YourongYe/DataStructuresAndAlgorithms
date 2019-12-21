# Example with recursion
```
def binarySearch(array, start_ind, end_ind, number):
    mid = (start_ind + end_ind)//2
    if number == array[mid]:
        return mid
    if start_ind >= end_ind:
        return -1
    
    if array[mid] > number:
        return binarySearch(array, start_ind, mid-1, number)
    else:
        return binarySearch(array, mid+1, end_ind, number)
    
array = [2,3,5,7,9,10,12,14,17]
print(binarySearch(array, 0, len(array)-1, 12))
print(binarySearch(array, 0, len(array)-1, 17))
print(binarySearch(array, 0, len(array)-1, 11))
```

# Result
```
6
8
-1
```
