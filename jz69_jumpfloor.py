# 跳台阶,解法1
class Solution:
    def jumpFloor(self , number: int) -> int:
        if number == 1:
            return 1
        else: # n > 1
            a, b = 1, 1  # 初始值
            for i in range(1,number): # 从n=2时循环一次
                a, b = b, a+b # a,b 交替更新
        return b
    
sol = Solution()
print(sol.jumpFloor(5))

# 解法2
class Solution:
    def jumpFloor(self , number: int) -> int:
        if number == 1 or number ==0:
            return 1
        else:
            number_list = [1,1]
            while number-1>0:
                number_list= [number_list[-1],number_list[-2]+number_list[-1]]
                number -=1
                # print(number_list)
            return number_list[-1]
        