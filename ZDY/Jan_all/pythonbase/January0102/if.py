#写一个程序，输入一个整数，判断这个整数是奇数还是偶数

x=int(input("请输入一个整数"))

if x % 2==1:
    print(x,'是奇数')
else:
    print(x,'是偶数')

#　输入一个数，作如下判断
#１）是否在５０到１００之间
#２）是否小于０

a=int(input('请输入一个数'))

if 50 <= a <= 100:
    print(a,'在５０到１００之间')
else:
    print(a，'不在５０到１００之间')

if a<0:
    print(a,'小于０')
else:
    print(a,'不小于０')