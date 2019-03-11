# 4.打印杨辉三角
# a=[]
# for i in range(10):
#     a.append([])
#     for j in range(10):
#         a[i].append(0)
# for i in range(10):
#     a[i][0]=1
#     a[i][i]=1
# for i in range(2,10):
#     for j in range(1,1+i):
#         a[i][j]=a[i-1][j-1]+a[i-1][j]
# for i in range(10):
#     for j in range(1+i):
#         print(a[i][j],'',end="")
#     print("\n") 
def get_next_line(L):
    '''此函数根据上一层Ｌ，返回下一层数字列表'''
    L2=[1]  #最左边的1
    # 计算中间的数字
    for i in range(len(L)-1):
        L2.append(L[i]+L[1+i])
    # 添加最后一个１
    L2.append(1)
    return L2
def get_yanghui_list(n):
    '''此函数返回ｎ层的杨辉三角的列表'''
    L=[]  #用来存放每一层的列表
    layer=[1]
    while len(L)<n:
        # 每次循环放入一层
        L.append(layer)
        layer=get_next_line(layer)  #算出下一层
    return L
def get_yanghui_string_list(L):
    '''传入一个数字列表，由数字列表组成的列表，返回字符串列表'''
    L2=[]  #准备存放字符串
    for layer in L:
        s=' '.join((str(x) for x in layer))
        L2.append(s)
    return L2
def print_yanghui_triangle(L):
    max_len=len(L[-1])
    for s in L:
        print(s.center(max_len))
L=print(get_yanghui_list(6))
string_L=get_yanghui_string_list(L)
print(string_L)
