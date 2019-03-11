# 现有一个已经设定好登录名和登录密码的系统，现有一用户忘记登录的
# 账号和密码，此登录系统只有３次尝试机会，请编写一个用户登录系统
#　如果在３次之内，当用户输入账号密码匹配，则登录成功，
# 否则登录失败，并且当你输入失败的情况下提示还剩几次机会
a ='1114265266'
b = '123456'
name = input("please input your name:")
key = input("please input your key:")
count = 0 #输入次数
i = 1 
if i <3 and name == a and key == b :
    print("loading is successful!")
else:
    while count < 3 :
        if i < 3 and name != a and key != b:
            print("fail! you only have",(3-i),"chances")
            name = input("please input your name:")
            key = input("please input your key:")
        elif i >= 3 :
            print("you have no chance!")
        i+=1
        count+=1
   

    


