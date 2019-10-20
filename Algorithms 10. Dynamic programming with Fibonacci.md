# Implementation
```py
memo = []
def fib(n):
    print(n)
    if n <= len(memo):
        return memo[n-1]
    if n == 1 or n == 2:
        result = 1
    else:
        #print(n)
        result = fib(n-2) + fib(n-1) # 注意这里n-2和n-1的顺序调换并不会影响append的顺序，但是function 被call的方式会改变
    memo.append(result) # 不能写成memo[n-1] = result的形式，因为python中的空array就是完全空的，而不是element=null
    return result

n = 8
#memo = [0]* (n+1)
print(fib(n))

```

# Concept
动态规划的核心在于以存量形式减少重复运算。每次recursion都先checkmemo中是否已经有结果，如果没有，才会继续运算
