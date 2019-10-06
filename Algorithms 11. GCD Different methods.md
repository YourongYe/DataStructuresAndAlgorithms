# 1. 辗转相减法
gcd（x，y）=gcd（x-y，y）

## Recursion
```py
def CommonDivisor_recursion(m, n):
    print(m,n)
    if m != n:
        return CommonDivisor_recursion(abs(m-n), min(m,n))
    else:
        return m

a = CommonDivisor_recursion(32,36)
print(a)
```
## Result
```py
32 36
4 32
28 4
24 4
20 4
16 4
12 4
8 4
4 4
4
```
## Iteration
```py
def CommonDivisor_iteration(m, n):
    while n != m:
        print(m,n)
        n, m = abs(m-n), min(m, n)
    return m


a = CommonDivisor_iteration(32,36)
print(a)
```

## Result
```py
32 36
32 4
4 28
4 24
4 20
4 16
4 12
4 8
4

```

# 2. 辗转相除法（又称欧几里得算法）

## Recursion
```py
def CommonDivisor_recursion(m, n):
    print(m,n)
    if min(m,n) == 0: # recursion 的退出机制通常都是用if else来写，其中一个condition需要return最后结果
        return max(m, n)
    else: # 一个condition需要return recursive functions
        return CommonDivisor_recursion(max(m,n)%min(m,n), min(m,n))

a = CommonDivisor_recursion(32,36)
print(a)
```

## Result
```py
32 36
4 32
0 4
4
```

## Iteration
```py
def CommonDivisor_iteration(m, n):
    m, n = max(m,n), min(m,n)
    while m % n != 0:
        print(m,n)
        n, m = m%n, min(m, n)
    return n


a = CommonDivisor_iteration(32,36)
print(a)
```

## Result
```py
36 32
4
```
