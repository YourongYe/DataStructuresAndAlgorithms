# Quick Sort
Basic idea is partition and recursion. And it is in-place (原地算法，不会用额外的数据结构，不会创建新的list).  

In each recursion, a 'pivot' will be selected. And the partition aims to swap all elements < pivot to the left,   
and all that > pivot to the right. 

Although it is in-place, taking no extra space for new variables, the recursive functions will take lots of stack space. 

# Time Complexity
**Best case & Average cases:** O(nlogn)   
**Worst case:** O(n<sup>2</sup>)  

## Way to improve and avoid worst case: 
**Rrandomised Quicksort**  
By randomly choosing the pivot, instead of choosing the last element, we can increase the chance of a balanced quicksort.  
One way to do it, is to choose the median as the pivot, and switch it with the last element, other things being equal.

# Example
```py
def Partition(A, start, end):
    pivot = A[end]
    pIndex = start
    for i in range(start, end):
        if A[i] < pivot:
            A[i], A[pIndex] = A[pIndex], A[i]
            pIndex += 1 # pIndex左边都是比pivot小的数
    A[pIndex], A[end] = A[end], A[pIndex]
    return pIndex

def QuickSort(A, start, end):
    print(A)
    if start < end:
        pIndex = Partition(A, start, end)
        QuickSort(A, start, pIndex-1)
        QuickSort(A, pIndex+1, end)
        
A = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
# A = [7,3,8,5,4,6]
start = time.time()
QuickSort(A, 0, 19)
print(time.time()-start)
```

# Another partition implementation
```py
def Partition(l1, start, end):
    pivot = l1[end]
    left = start
    right = end - 1
    while left <= right:
        while (l1[left] < pivot) and (left <= end):
            left += 1
        while (l1[right] > pivot) and (right >= start):
            right -= 1
        if left < right:
            l1[left], l1[right] = l1[right], l1[left]
    l1[left], l1[end] = l1[end], l1[left]
    return left
```
# Result
```py
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
[1, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 20]
[1, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 20]
[1, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 20]
[1, 2, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 19, 20]
[1, 2, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 19, 20]
[1, 2, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 19, 20]
[1, 2, 3, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 18, 19, 20]
[1, 2, 3, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 18, 19, 20]
[1, 2, 3, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 18, 19, 20]
[1, 2, 3, 4, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 17, 18, 19, 20]
[1, 2, 3, 4, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 17, 18, 19, 20]
[1, 2, 3, 4, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 14, 13, 12, 11, 10, 9, 8, 7, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 14, 13, 12, 11, 10, 9, 8, 7, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 14, 13, 12, 11, 10, 9, 8, 7, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 13, 12, 11, 10, 9, 8, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 13, 12, 11, 10, 9, 8, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 13, 12, 11, 10, 9, 8, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 12, 11, 10, 9, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 12, 11, 10, 9, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 12, 11, 10, 9, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
0.0003159046173095703
```

# A faster QuickSort function
If we change a little bit in QuickSort function, with the same partition function  
the function called times will be reduced, save nearly half of time
```py

def QuickSort(A, start, end):
    print(A)
    while start < end: # here changes into 'while' rather than 'if'
        pIndex = Partition(A, start, end)
        QuickSort(A, start, pIndex-1)
        start = pIndex + 1
```
In the first version using 'if', the function called times increase exponentially  
But for the second version using 'while', multiple times of partition can be done in the same QuickSort function.  
The partition times might be the same, but part of stack space will be released due to less recursion.

# Result
```py
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
[1, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 20]
[1, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 20]
[1, 2, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 19, 20]
[1, 2, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 19, 20]
[1, 2, 3, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 18, 19, 20]
[1, 2, 3, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 18, 19, 20]
[1, 2, 3, 4, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 17, 18, 19, 20]
[1, 2, 3, 4, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 14, 13, 12, 11, 10, 9, 8, 7, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 14, 13, 12, 11, 10, 9, 8, 7, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 13, 12, 11, 10, 9, 8, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 13, 12, 11, 10, 9, 8, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 12, 11, 10, 9, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 12, 11, 10, 9, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
0.00019598007202148438
```



