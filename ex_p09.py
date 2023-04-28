def binary_search(li, val): 
    left = 0
    right = len(li) - 1 # 列表最后一个元素的索引
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val: # 候选区更新为mid的左边
            right = mid - 1
        else: # li[mid] < val, 候选区在右边
            left = mid + 1
    else: # while循环结束，不满足while循环条件
        return None
    
li = [1,2,3,4,5,6,7,8]
print(binary_search(li,8))