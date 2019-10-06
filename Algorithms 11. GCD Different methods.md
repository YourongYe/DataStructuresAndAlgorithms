# 辗转相减法
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

