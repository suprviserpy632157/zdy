# 顺序查找练习
# 原始数据
# 待查找数据
def liner(data,key):
    for i in range(len(data)):
        # 对比当前数据与待查找数据
        if data[i] == key:
            # 查找成功,返回下标值
            return i
    else:
        # 遍历完仍未找到数据
        return -1

if __name__ == '__main__':
    # 原始数据
    value = [8,3,1,6,7,5,2,13,12,4,11,10,9]
    # 待查找数据
    key = 8
    # 获取返回结果并输出
    res = liner(value,key)
    if res == -1:
        print('查找失败')
    print('查找成功,是第%d张'%(res + 1))