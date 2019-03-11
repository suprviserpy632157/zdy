# 二分查找练习,递归实现
# 当前查找范围的首元素和尾元素下标值(left,right)
def binarysearch(value,key,left,right):
    # 递归的退出条件
    if left > right:
        # 查找结束,为找到
        return -1
    # 获取中间元素对应下标值
    middle = (left + right) // 2
    # 对比中间元素与查找元素
    if value[middle] == key:
        # 查找成功
        return middle
    elif value[middle] > key:
        # 若中间元素大于待查找元素值则在左侧继续查找
        # 查找范围减半:左侧下标值不变,右侧下标值变为middle-1 
        return binarysearch(value,key,left,middle-1)
    else: 
        # 若中间元素小于待查找元素值,则在右侧继续查找
        # 查找范围减半:右侧下标值不变,左侧下标值变为middle+1
        return binarysearch(value,key,middle+1,right)
if __name__ == "__main__":
    # 原始数据
    value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    # 待查找数据
    key = 6
    res = binarysearch(value,key,0,len(value)-1)
    if res == -1:
        print("查找失败")
    print("查找成功,是第%d张"%(res+1))