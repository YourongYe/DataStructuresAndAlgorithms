# Quick Sort
Basic idea is partition and recursion. And it is in-place (原地算法，不会用额外的数据结构，不会创建新的list).  

In each recursion, a 'pivot' will be selected. And the partition aims to swap all elements < pivot to the left,   
and all that > pivot to the right. 

Although it is in-place, taking no extra space for new variables, the recursive functions will take lots of stack space. 

# Example
```py
def Partition(A, start, end):
    pivot = A[end]
    pIndex = start
    for i in range(start, end):
        if A[i] < pivot:
            A[i], A[pIndex] = A[pIndex], A[i]
            pIndex += 1
    A[pIndex], A[end] = A[end], A[pIndex]
    return pIndex

def QuickSort(A, start, end):
    print(A)
    while start < end:
        pIndex = Partition(A, start, end)
        QuickSort(A, start, pIndex-1)
        start = pIndex + 1
        QuickSort(A, pIndex+1, end)
```

# Result

