# Recursion 写法：
## 1. 如果题目是想要找到一个最终值，即想return的是最后那个点相关的值，那么就应该写成下面的形式：
```py
def DFS(root, depth, value):
    if not root: return
    if root.val == value:
        global res
        res = depth
        return
    if root.val > value:
        DFS(root.left, depth+1, value) # function 并没有return任何东西，但是传的值一直在改变，当这个值改变到某个时刻符合了我们的条件，那我们就用一个外部变量来接住这个值
    else:
        DFS(root.right,depth+1, value)
```
即用一个外部变量来接最终得到的结果，这样就不用return任何东西，而return的值也不会在recursion中途不停地改变
这种外部变量尤其适用于当我们需要keep track of 多个变量的时候，因为如果只有一个变量我们可以直接把它作为func的return值，比如：
```py
def DFS(root, depth, value):
    if not root: return
    if root.val == value:
        return depth
    if root.val > value:
        return DFS(root.left, depth+1, value) # 只return最终的那个值
    else:
        return DFS(root.right,depth+1, value)

res = DFS(root, 0, x)
#res = DFS(root, 0, y)
print(res)
```

## 2. 如果题目是要划范围，即相同的情况就会一直dfs，不相同就break（典型的题：number of islands）,则什么都不用return
```py
def dfs(i,j):
    if grid[i][j] == '1':
        grid[i][j] = '0'
        dfs(i+1, j)
        dfs(i, j+1)
        dfs(i-1, j)
        dfs(i, j-1)
```
以上为简易版本，大致逻辑是对的  
只有什么都不用return的情况，才可以连着call多个dfs(), 如果有return的值，则必须每个call之前都写上一个condition  

## 3. Recursion 参数
###Recursion func的参数通常包括   
1）要assess的那个值或者那个点    
2）要定位的那个值，每次都会变，比如root，比如i,j，比如一个list的index，比如quicksort里的start，end  
3）background背景框架，可能要变，也可能不变，比如quicksort里的array，比如grid，matrix等等 （有时可以作为global variable，不用传参）

Eg. 在Number of islands题中，i,j既是定位的参数，也是要assess的参数
Eg. 在Quicksort中，要assess的点是每次[start:end]的pivot点，定位也是start和end，而background则是array本身，也是会改变的

## 4. Recursion 写法
1. 终止条件：  
1） 该点的值不满足条件：比如root或者node为None， 比如grid[i][j] != 1  
2） 找到了满足条件的点，不用再继续找了  
2. 继续条件：
1） 一般为除了终止条件以外的其他情况  

注意：有时可以省略终止条件，如果不满足继续的条件则func会自动return，这种方法通常适用于不需要return任何结果的情况，  
如果需要return结果则一定要写终止条件  



