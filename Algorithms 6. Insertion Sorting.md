# Insertion Sorting
As its name suggests, try to put each element in tht right position by inserting.

Although it's insert, it does not necessarily mean insert one element and shift others. 

Two methods are shown: Swap and shift

# Difference between Insertion Sort and Bubble Sort
Bubble sort: 每次循环没有明确的目标，就是在途中遇到的最大的值会被挪到最后  
Insertion sort：每次outter iteration都有target，就是第i个element，目的是把第i个element挪到right position  

# Example
```py
import time

def insertionSort(A): # this sort using swap
    for i in range(1, len(A)): # i means which element I'm gonna insert this time, 第一个数前面没有可以insert的地方，所以从第二个数开始
        j = i - 1 # target和target前一个数开始比较
        while A[j] > A[j+1] and j >= 0: # j>=0不能少，因为如果此次循环的target是整个list中最小值，那么当被挪到第一位时，j-1=-1此时不应该再进入循环
            A[j], A[j+1] = A[j+1], A[j] # by swapping till reaching its right position
            j -= 1 # 
    return A
    
# 每次outter循环都，i前面的数都已经是in order
    
def insertionSort1(A):
    for i in range(1, len(A)):
        temp_num = A[i]
        j = i - 1
        while A[j] > temp_num and j >= 0:
            A[j+1] = A[j] # 不同点在于上面的写法要switch，涉及到两个值的改动，还有程序内部第三个temp值（swap中都有），而这里每次只会涉及到一个值的改变，
            j -= 1
        A[j+1] = temp_num # 当inner iteration结束，一定要把target值放回right position
    return A
    
# 下面这种写法在inner iteration时会节约大概一般的时间

B = [10,9,8,7,6,5,4,3,2,1]

start = time.time()
print(insertionSort(B))
print('Swap using time: ', time.time()-start)
start = time.time()
print(insertionSort1(B))
print('Shift using time: ', time.time()-start)
```

# Result
```py
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Swap using time:  5.817413330078125e-05
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Shift using time:  8.821487426757812e-06
```
