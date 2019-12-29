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



## 5. Counter recursion 题型的写法
1. Implicit counter： 在终止条件里初始化为0, 不作为参数传入，而是直接在return结果时进行累加  
```py
def DFS(root):
    if not root: return 0
    return max(DFS(root.left)+1, DFS(root.right)+1) #func本身参与运算
```
在终止条件里return结果，只适用于当终止条件=我们想要找的结果的终止点  
比如：上面的例子中，我们想要计算每一个分支的depth，所以当root为空时，我们对每个分支的search就会结束，而这一个node刚好是计算depth的最终点  
再比如：在Number of islands （max area） 的例子中，当一个点的上下左右都不是1时，我们知道这个点就是current island的其中一个边界点。但是我们要穷尽每一个边界点，所以终止条件并非最终点，所以我们不能在终止条件里return一个起始值0.这就不同于上面的例子，我们可以确定最终点在哪儿，以及最终点的值。island的最终点可以是任意一个边界点。

2. Explicit counter：counter以参数形式初始化，将0传入，然后每次传参时累加
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
        DFS(root.right,depth+1, value) # func本身不参与任何运算，仅仅用于call一个operation
```
最后return的值可以选择用外部变量接住（当有多个变量需要return的时候），或者直接return（一个变量）

```py
def DFS(root, depth, value):
    if not root: return
    if root.val == value:
        return depth
    if root.val > value:
        return DFS(root.left, depth+1, value) # 只return最终的那个值
    else:
        return DFS(root.right,depth+1, value) # func本身不参与运算
res = DFS(root, 0, x)
```
3. Explicit counter： counter在函数内部初始化，累加，然后return
```py
def dfs(grid,i,j):
    grid[i][j]=0
    area=1
    if i+1<n and grid[i+1][j]==1:
        area+=dfs(grid,i+1,j) # func本身参与运算，作为累加项
    if i-1>=0 and grid[i-1][j]==1:
        area+=dfs(grid,i-1,j)
    if j+1<m and grid[i][j+1]==1:
        area+=dfs(grid,i,j+1)
    if j-1>=0 and grid[i][j-1]==1:
        area+=dfs(grid,i,j-1)
    return area
```
虽然每次call这个func时，area都会初始化为1，但是可以看成是每到一个点，就以这个点为中心，计算上下左右的1，每个func return的area都是这个点以及他周围的1

4. Implicit counter: boolean也可以看作是一种counter，记录整个assess的过程是否有invalid情况。
```py
def recursion(string):
    if not string: return True
    for i in range(1, max_length+1):
        if string[:i] in word_dict and recursion(string[i:]): # 当需要把传入的变量break down然后对各个部分进行assess的时候，可以写成这样
            return True
    return False
```
一般如果题目要求返回boolean，recursion func就应该写成return true或者false的情况。这种题型在特殊的时候，recursion func可以作为if statement的一部分出现
```py
def recursion(string):
    if not string: return True
    for i in range(1, max_length+1):
        if string[:i] in word_dict: 
            return recursion(string[:i])
    return False
```
与上面的func的区别在于，这个func只会assess一种情况（每个substring都最短的情况，比如同时有'app'和'apple'就只会找'app'）而非所有情况
比如word_dict = ['read', 'readable']  
那么'reaable’就会被拆开成 --> 'read' + 'able'， 因为找不到‘able’所以会返回false，但实际上应该返回true
