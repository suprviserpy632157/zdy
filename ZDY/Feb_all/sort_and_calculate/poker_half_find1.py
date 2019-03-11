# 二分查找练习,循环实现
# 当前查找范围的首元素和尾元素下标值(left,right)
def binarysearch(value,key):
    # 获取当前数据的左侧/右侧的下标值
    left = 0
    right = len(value) - 1
    # 若存在合法的范围则继续查找
    while left <= right :
        # 获取中间值
        middle = (left + right) // 2
        # 比较查找值与中间值
        if value[middle] == key:
            # 查找成功
            return middle
        elif value[middle] > key:
            # 若中间值大于查找值,继续在左侧查找:左侧下标值不变,右侧变为middle的前一位
            right = middle -1
        else:
            # 若中间值小于查找值,继续在右侧查找:右侧下标值不变,左侧变为middle的后一位
            left = middle + 1
    # 遍历完所有数据仍未找到
    return -1
if __name__ == "__main__":
    # 原始数据
    value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    # 待查找数据
    key = 6
    res = binarysearch(value,key)
    if res == -1:
        print("查找失败")
    print("查找成功,是第%d张"%(res+1))