# 选择排序，每次选列表中最大或最小的数
def select_sort_simply(li): 
    li_new = [] # 存储列表
    for i in range(len(li)): # 遍历列表每个值
        min_val = min(li)  # 列表最小值，用函数min()
        li_new.append(min_val) # 添加到列表末尾
        li.remove(min_val) # 移除指定的值
    return li_new

li = [3,2,4,1,5,6,8,7,9]
print(select_sort_simply(li))

# 选择排序优化
def select_sort(li): 
    for i in range(len(li)-1): # 运行次数，最后一趟不需要遍历
        min_loc = i # 定义变量记录无序区中最小值的位置，起始位置为无序区的第1个数
        for j in range(i+1, len(li)): # 无序区范围为(i,n),其中i表示的是元素的索引值， 最后一个数值的索引值为n-1
            if li[min_loc] > li[j]:
                min_loc = j # 记录最小值的索引
        li[i], li[min_loc] = li[min_loc],li[i]  # 将最小值提到无序区的第一位
    
    print(li)

lis = [2,8,6,4,9,3,5]
select_sort(lis)


