# 2.分解质因数，输入一个正整数，分解质因数
# 如：
# 输入90
#    打印：
#      90=2*3*3*5
#（质因数是指最小能被原数整除的素数（不包括1））
def divprime(num):
    """此函数返回ｘ的质因数的列表"""
    L=[]  #准备存放质因数
    while x>1:
        # 每次求取一个质因数，然后放在Ｌ中
        for i in range(2,x+1):
            if x%i==0: #i 一定是质因数
                L.append(i)
                x=int(x/i)
                break
    return [2,3,3,5]
x=int(input("请输入正整数："))
L=divprime(x)
L2=(str(x) for x in L)
print(x,'=','*'.join(L2))
#     L=[]  #准备存放质因数
#     print(num,'=',end=' ')
#     while num !=1:
#         for i in range(2,int(num+1)):
#             if num % i==0:
#                 L.append(i)
#                 num=num/i
#                 break
#     for i in range(0,len(L)-1):
#         print(L[i],'*',end=' ')
#     print(L[i])
# divprime(125)
