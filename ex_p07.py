# 顺序查找
def linear_search(li, val): # li：列表，val：查找的值
    for i, v in enumerate(li):  # 遍历索引和值
        if v == val:
            return i
    else: # 结束循环后执行
        return None
    
li = [1,4,8,3,2,6,5]
print(linear_search(li, 6))