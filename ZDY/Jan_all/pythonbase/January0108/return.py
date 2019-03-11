# 此实例示意return语句在函数中的应用
# 与ｂｒｅａｋ的区别在于一个终止函数，
# 一个终止循环
def say_hello2():
    print("hello aaa")
    print("hello bbb")
    # return # ==return None 
    return [1,2,3,4]
    print("hello ccc")
v=say_hello2()
print("v=",v)
v2=say_hello2()
print("v2",v2)