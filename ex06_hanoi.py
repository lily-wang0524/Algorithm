# 汉诺塔问题

def hanoi(n,a,b,c): # param:n-圆盘个数；(a,b,c):圆盘从a移动到c经过b
    if n > 0: 
        hanoi(n-1, a, c, b)  # n-1个圆盘从a经过c移动到b
        print("moving from %s to %s" % (a,c)) # 从a移动到c
        hanoi(n-1, b, a, c) # n-1个圆盘从b经过a移动到c

# hanoi(3, 'A', "B", 'C')

# 移动次数
class hanoi_num(): # 汉诺塔移动次数
    def __init__(self):
        self.x = 0  # 初始次数，变量是具体的则该变量不属于参数

    def hanoi(self, n, a, b, c): # 汉诺塔移动
        if n > 0:
            self.hanoi(n-1, a, c, b)
            print(f"moving {a} to {c}")
            self.x += 1
            self.hanoi(n-1, b, a, c)
        
num = hanoi_num()# 实例化类
num.hanoi(7,'A','B','C') 
print(num.x)

# 递推式计算h(x)=2h(x-1)+1
def hanoi_len(n):
    if n == 0:
        return 0
    else:
        return hanoi_len(n-1) * 2 + 1

len = hanoi_len(7)
print(len)