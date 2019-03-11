# 2.完全数：
#   1+2+3=6（6为完全数）
#   1,2,3因为都是6的因数
# （能被一个数x整除的数为y，则y为x的因数）
#   1x6=6
#   2x3=6
# 完全数是指除自身以外的所有因数之和相加等于自身的数
# 求4~5个完全数并打印：
# 答案：6 28 496…
# def factors(n):
#     return [i for i in range(2,n/2+1) if n%i==0]    
# def perfect(n):
#     return [i for i in range(2,n+1) if (sum(factors(i))+1)==i]
# if __name__=="__main__":
#     print perfect(1000)
#     print factors(1000)
# l=[]
# for n in range(1,10000):
#     for a in range(1,n):
#         if n%a==0:
#             l.append(a)
#     if sum(l)==n:
#         print(l)
#         print(n)
#     l=[]
def is_perfect_number(x):
    "此函数判断ｘ是否为完全数"
    #创建一个列表，用来存放ｘ所有的因数
    L=[]
    for i in range(1,x):
        #整除了，ｉ则一定是ｘ的因数
        if x%i==0:
            L.append(i)
    #是完全数
    if sum(L)==x:
        return True
    return False
def main():
    i=2
    while True:
        #如果ｉ是完全数，则打印ｉ的值
        if is_perfect_number(i):
            print(i)
        i+=1
main()