#次实例示意try_except.py
def div_apple(n):
    print(n,'个苹果你想分给几个人？')
    s=input("请输入人数:")
    cnt=int(s)  #可能触发ValueError错误
    result=n/cnt  #可能触发ZeroDivisionError错误
    print("没人分了",result,"个苹果")

try:
    div_apple(10)
    print("分苹果成功")
except ValueError:
    print("分苹果失败，苹果被回收")
except ZeroDivisionError:
    print("没有人来，苹果自己吃了!")
print("程序正常退出")