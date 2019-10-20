```py
def maxDifference(array):
    dmax = -1
    vmin = array[0]
    for i in range(1, len(array)):
        if array[i] < vmin:
            vmin = array[i]
        elif array[i] - vmin > dmax:
            dmax = array[i] - vmin
    return dmax

a = [-2,5,3,7,9,1,55,3]
b = [8,7,6,5,4,3]
print(maxDifference(a))
print(maxDifference(b))

def maxDifference1(array):
    dmax = -1
    vmax = array[-1]
    for i in range(len(array)-1, 0, -1):
        if array[i] > vmax:
            vmax = array[i]
        elif vmax - array[i] > dmax:
            dmax = vmax - array[i]
    return dmax

a = [2,5,3,7,-9,1,55,3]
b = [8,7,6,5,4]
print(maxDifference1(a))
print(maxDifference(b))
```

# Result
```py
57
-1
64
-1
```
