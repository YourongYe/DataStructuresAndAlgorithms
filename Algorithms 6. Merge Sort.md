```py
def MergeSort(array):
    if len(array) > 1:
        middle_index = len(array)//2 # 找到一个中点来break成两部分
        leftside = MergeSort(array[:middle_index]) # 和quicksort不同在于，每一次recursion都create了两个新的list
        rightside = MergeSort(array[middle_index:])
        return Merge(leftside, rightside)
    else:
        return array

def Merge(leftside, rightside):
    newlist = []
    i = 0
    j = 0
    while i < len(leftside) and j < len(rightside): # 用到two pointers的概念，把两个list合成一个
        if leftside[i] <= rightside[j]:
            newlist.append(leftside[i])
            i += 1
        else:
            newlist.append(rightside[j])
            j += 1
    if i < len(leftside):
        newlist = newlist + leftside[i:] # 把剩下没insert的那个list剩下的部分加进去
    if j < len(rightside):
        newlist = newlist + rightside[j:]
    return newlist


array = [8,7,6,5,4,3,2,1]
print(MergeSort(array))
```
