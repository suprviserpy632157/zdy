a=100
b=200
s=input("请输入字符串a+b：")
m=eval(s)
n=exec(s)
print(m)
print(n)

L1=[x for x in map(lambda x,y:x+y,[1,2,3,4],[5,6,8])]
print(L1)
for x in filter(lambda x:x%2==1,L1):
    print(x)