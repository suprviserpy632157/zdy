#试写一个生成器函数myfilter，要求此函数域系统内
# 建的filter函数功能完全一致
def myfilter(fn,iterable):
    for x in iterable:
        if fn(x) == True:
            yield x
for y in myfilter(lambda x :x%2==0,range(10)):
    print(y)