# break 语句
# i=1
# while 1<=6:
#     print("begin:",i)
#     if i==3:
#         break
#     print("end:",i)
#     i+=1
# else:
#     print("这是ｗｈｉｌｅ语句中的ｅｌｓｅ字句")
# print("程序结束")
# 循环嵌套中的ｂｒｅａｋ,原本是打印１到２０
j=1
while j<=10:
    i = 1
    while i<=20:
        print(i,end=' ')
        if i==15:
            break
        i += 1
    print()
    j+=1