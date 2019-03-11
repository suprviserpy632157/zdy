# myenumerate.py
def myenumerate(iterable,start=0):
    # 方法1 用while语句实现
    # it=iter(iterable) #拿到迭代器
    # while 1:
    #     try:
    #         v=next(it)
    #         yield(start,v)
    #         start+=1
    #     except StopIteration:
    #         return
    # 方法2 用for语句实现
    for v in iterable:
        yield (start,v)
        start+=1
L=[3,5,8,10]
for i,v in myenumerate(L):
    print('索引为',i,'的元素值为',v)




