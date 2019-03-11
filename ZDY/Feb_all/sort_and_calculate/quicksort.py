# 快速排序
# 原始数据
# value = [55,49,10,6,78,44,33,55,66,88]
def quick(value):
    # 递归退出条件
    # 即仅剩一个元素无需继续分组
    if len(value) < 2:
        return value
    # 设置关键数据
    A = value[0]
    # 找出所有比A大的数据
    big = [x for x in value if x > A]
    # 找出所有比A小的数据
    small = [x for x in value if x < A]
    # 找出所有比A相等的数据
    equal = [x for x in value if x == A]
    # 拼接数据排序的结果
    return quick(small) + equal + quick(big)
if __name__ == "__main__":
     # 原始数据
    value = [55,49,10,6,78,44,33,55,66,88]
    # 快速排序
    print("begin sort:",value)
    after = quick(value)
    print("behind sort:",after)