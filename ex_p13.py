# 冒泡排序
def bubble_sort(li): # li为列表
    for i in range(len(li) - 1):  # 总共排序趟数
        for j in range(len(li) - i - 1): # 每趟运行的次数
            if li[j] > li[j+1]: # 后一个数小于前一个数
                li[j], li[j+1] = li[j+1],li[j]

li = [3,6,4,8,9,2,1]
bubble_sort(li)
print(li)


# 冒泡排序改进
def bubble_sort1(li): # li为列表
    for i in range(len(li) - 1):  # 总共排序趟数
        exchange = False   # 是否交换
        for j in range(len(li) - i - 1): # 每趟运行的次数
            if li[j] > li[j+1]: # 后一个数小于前一个数
                li[j], li[j+1] = li[j+1],li[j]
                exchange = True # 位置交换
        print(li)
        if not exchange:  # 位置未发生交换
            return
        
lis = [4,6,3,2,7,8,9]
bubble_sort1(lis)

