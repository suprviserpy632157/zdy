# 写一个程序，任意输入一个整数，判断这个数是否是素数（prime）打印结果
# num = int(input("Please input a nunmber:"))
# if num>1:
#     for i in range(2,num):
#         if (num%i)==0:
#             print(num,"not prime")
#             break
#     else:
#         print(num,"prime")
# else:
#     print(num,"not prime")
# def is_prime(x):
#     if x > 1:
#         for i in range(2,x):
#             if(x%i)==0:
#                 print(x,"not prime")
#                 break
#         else:
#             print(x,"prime")
#     else:
#         print(x,"not prime")

# l=[]
# for i in range(3,100):
#     if is_prime(i) == True:
#         l.append(i)
#     else:
#         pass
# print(l)

x=int(input("Please input a nunmber:"))
if x<2:
    print(x,'no prime')
else:
    flag = True  #标志
    for i in range(2,x):
        if x%i==0:
            print(x,'no prime')
            flag =False
            break
    if flag:
        print(x,"prime")
