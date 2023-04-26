def Fibonacci(n): # n个数
    if n < 2: # n = 0或1
        return n  # 返回本身
    else:  # n > 2
        a, b = 0, 1  # 初始值
        for i in range(n - 1): # n=0和n=1 不需要循环
            a, b = b, a+b
    return b

print(Fibonacci(5))
