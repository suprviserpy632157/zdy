# ５．输入三个整数，请把这三个数由小到大输出
# num1 = int(input("请输入第一个数："))
# num2 = int(input("请输入第二个数："))
# num3 = int(input("请输入第三个数："))
# if num1 < num2 and  num1 < num3:
#     if num2 < num3:
#         print(num1,num2,num3)
#     else:
#         print(num1,num3,num2)
# elif num2 < num3 and num2 < num1:
#       if num3 < num1:
#           print(num2,num3,num1)
#       else:
#           print(num2,num1,num3)
# elif num3 < num1 and num3 < num2:
#       if num1 < num2:
#           print(num3,num1,num2)
#       else:
#           print(num3,num2,num1)
# else:
#     pass
a = int(input("please input a number:"))
b = int(input("please input a number:"))
c = int(input("please input a number:"))
# x=a
# if x>b:
#     x = b
# elif x>c :
#     x = c
# y = b
# if y<a:
#     y=a
# elif y<c :
#     y=c
y=max(a,b,c)
x=min(a,b,c)
z=0
if  a!=x and a!=y :
    z=a
elif b!=x and b!=y:
    z=b
elif c!=x and c!=y:
    z=c
print(x,z,y)

l=[]
for i in range(3):
    s = int(input("please input a number:"))
    l.append(s)
l.sort()
print(l)


    