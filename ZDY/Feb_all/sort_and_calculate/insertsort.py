# 直接插入排序
# 原始数据value
# []
def insert(value):
    # 外层循环:对应所有无序数据,找出插入数据
    for i in range(1,len(value)):
        # 备份取出的数据
        temp = value[i]
        # 记录取出时的下标值
        pos = i
        # 内层循环:对应从后向前扫描所有有序数据
        # 1->从最后一个有序数据开始,即无序数据前一位
        # 2->包含扫描到下标为0为止
        # 3->从后向前扫描
        for j in range(i-1,-1,-1):
            # 若有序数据大于取出数据
            if value[j] > temp:
                # 有序数据后移
                value[j+1] = value[j]
                # 更新数据的插入位置
                pos = j #j = i-1 对应所有有序数据比取出数据打的情况
            #  若有序数据小于等于取出数据
            else:
                # 更新数据的插入位置
                pos = j + 1
                break
        # 在指定位置插入数据
        value[pos] = temp
if __name__ == '__main__':
    # 原始数据
    value = [300,209,286,248,258,215,288,299,180,250]
    # 插入排序
    print("begin sort:",value)
    insert(value)
    print("behind sort:",value)
    