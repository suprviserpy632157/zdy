# 练习：
# 写一个函数get_age用来获取一个人的年龄信息
# 此函数规定用户只能输入1~140之间的整数，如果
# 用户输入其它的数则直接触发ValueError类型的错误
# def get_age():
#     age=int(input("please input an age(1~140)："))
#     if age<1 or age>140:
#         raise ValueError("over range")
#     return age
# try:
#     age=get_age()
#     print("you input age is:",age)
# except ValueError as e:
#     print("e=",e)
#     print("you input exe is error")

# 练习
# 有一个集合：
# 用for语句来遍历所有元素如下
s={'唐僧','悟空','八戒','沙僧'}
# for x in s:
#     print(x)
# else:
#     print("遍历结束")
it=iter(s)
while 1:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        print("遍历结束")
        break

