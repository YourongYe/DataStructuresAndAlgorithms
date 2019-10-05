# Key idea for each method
## Bubble Sort:   
Two layers of loops needed.  
Each outter iteration will send the biggest number to the end (first loop to first end, second loop to second end).  

## Insertion Sort:
Two layers of loops needed.
Each outter iteration will insert the target number to its right position (并不是序号和最后结果一致，而是i之前的数一定是in order)  
相当于从第一个数开始取，然后重新排序，但是是in-place（原地算法）

## Quick Sort:
分成两个function：  
Partition (需要找一个pivot，并返回pIndex：pivot最后的位置)
QuickSort （每次传入的都是同一个list，所以知道pIndex非常重要，pIndex会将list分割成无数sublist来deal with）

Partition中会有一个loop，QuickSort中以recursion为主，想提高速度时可加上while loop

Each loop in partition aims to swap the smaller number (than pivot) to the left
