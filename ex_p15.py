# 插入排序
def insert_sort(li):

    for i in range(1,len(li)): # 范围[1,n]
        j = i - 1 # j是指针，最开始的位置是有序区的最后一位，之后逐步往左移
        tmp = li[i] # 当前手上摸到的牌,因为列表中的数值会不断往后填充，为了不被覆盖掉，要单独保存

        while j >= 0 and li[j] > tmp: # 指针j还在有序区内，并且存在j指向的值大于摸到的牌
            li[j+1] = li[j] # j指向的元素往后移动
            j -= 1 # 指针往左移动

        li[j+1] = tmp  # 跳出循环后，j被减一了，指向了前一个比tmp小的数值，因此tmp的位置应该是j+1

li = [2,4,6,8,3,9]
insert_sort(li)
print(li)