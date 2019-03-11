# 输入年龄，判断是否是成年人。
#     如果是成年人，“恭喜您，已成年！”
#     否则，“未成年人”。
age = int(input("please give an age:"))
if age > 18 :
    print("you're an adult ")
else:
    print("you're a teenager")

# 定义一个表示季节的变量,
#   在每个case中对应不同的季节,
#   打印对应特点 
reason = input("please give a reason:")
if reason == 'spring':
    print(reason,"is coming!")
elif reason == 'summer':
    print(reason,"I want to eat icecream")
elif reason == "autumn":
    print('I like ',reason)
elif reason ==  "winter":
    print("My favorite reason is",reason)
else:
    print("please input a correct season!")