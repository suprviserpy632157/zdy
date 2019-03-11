# 2.已知有列表：
# L=[[3,5,8],10,[[13,14],15,18],20]
# 1）写一个函数print_list(lst)打印出所有的数字
#    如：print_list（L） #3  5  8  10  13  14
# 2）写一个函数sum_list(lst)返回这个列表中所有数字的和
#    如：print_sum(L)  #  106
#    注：type（x）可以返回一个变量的类型，
#    如：
#    >>>type(20) is int   #True
#    >>>type([1,2,3]) is list  #True
L=[[3,5,8],10,[[13,14],15,18],20]
def print_list(lst,newline=False):
    for x in lst:
        if type(x) is list:
            print_list(x)
        else:
            print(x,end=" ")
    if newline:
        print()
print_list(L,True)
def sum_list(lst):
    s=0
    for x in lst:
        if type(x) is list:
            s+=sum_list(x)
        else:
            s+=x
    return s
print(sum_list(L))
