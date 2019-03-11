# 1.写一个生成器函数myrange(start,stop,step)来生成一系列整数
# 要求：
# myrange的功能与range功能完全相同
# 不允许调用range函数和列表
#   用自己写的myrange结合生成器表达式求1~10内的奇数的平方和
#   
def myxrange(start,stop=None,step=1):
    if stop is None:
        stop=start
        start=0
    L=[]
    if step > 0 :
        while start<stop:
            L.append(start)
            start+=step
    elif step<0:
        while start>stop:
            L.append(start)
            start+=step
    return L
print(sum((x for x in myxrange(1,10) if x%2==1 )))
print(sum((x for x in range(1,10) if x%2==1 )))