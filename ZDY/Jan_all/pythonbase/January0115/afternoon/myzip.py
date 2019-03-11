# myzip.py
# 此实例示意用生成器函数来创建一个与
# ｚｉｐ函数功能一致的函数
def myzip(iterable1,iterable2):
    it1=iter(iterable1) #拿到第１个参数的迭代器
    it２=iter(iterable２) #拿到第２个参数的迭代器
    while 1:
        try:
            v1=next(it1)
            v2=next(it2)
            yield(v1,v2)
        except StopIteration:
            return
names=['中国移动','中国电信','中国联通']
numbers=[10086,10000,10010,95588]
for t in myzip(numbers,names):
    print(t)