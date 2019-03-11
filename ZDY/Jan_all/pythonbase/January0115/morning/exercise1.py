#写一个生成器函数myeven(begin,end),
# 用来生成从begin开始到end结束的
# 所有与偶数（不包含end） 
def myeven(begin,end):
    while begin<end:
        if begin%2==0:
            yield begin
        begin+=1
for x in myeven(1,10):
    print(x)
L=[x**2 for x in myeven(4,9)] 
print(L)  