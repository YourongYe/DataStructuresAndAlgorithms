def binomialCoef(n, k):
    if n == k:
        return 1
    if n == k+1:
        return n
    result = 1
    for i in range(1, n+1):
        result *= i
        if i == n-k:
            div1 = result
        if i == k:
            div2 = result
    return result/(div1*div2)

print(binomialCoef(10,5))

def binomialCoef1(n, k):
    if n == k:
        return 1
    if n-k < k:
        k = n-k
    array = [1,1] + [0]*(k-1)
    for i in range(n-1):
        temp = array[0]
        for j in range(1,k+1):
            temp, array[j] = array[j], array[j] + temp
    return array[-1]

print(binomialCoef1(10,5))


# 优化版
def binomialCoef1(n, k):
    if n == k:
        return 1
    if n-k < k:
        k = n-k
    array = [1] + [0]*(k-1)
    for i in range(n-1):
        temp = 1
        for j in range(0,k):
            temp, array[j] = array[j], array[j] + temp
    return array[-1]

print(binomialCoef1(10,5))
